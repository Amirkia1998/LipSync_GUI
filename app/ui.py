import webbrowser
import gradio as gr
import os

# Gradio paths are paths to temporary files (copy of the original) which get deleted after the program is closed
# The files are located in the server where gradio app is running
def generate_video(face_path, audio_path, model_name, resize_factor=1, pads="0 10 0 0", filename="result"):
    current_dir = os.getcwd()
    os.chdir("..\\wav2Lip")

    inference_script = "inference.py"
    model_path = f"checkpoints\\{model_name}.pth"
    output_path = f"..\\app\\results\\{filename}.mp4"

    command = f"""
        python {inference_script} \
        --checkpoint_path {model_path} \
        --face {face_path} \
        --audio {audio_path} \
        --resize_factor {resize_factor} \
        --pads {pads} \
        --outfile {output_path}
        """

    return_code = os.system(command)
    if return_code == 0:
        print("\n======== The video was generated successfully ========\nVideo saved at: " + output_path)
        print("======================================================")
        return output_path
    else:
        return "Error during video generation"

def show_folder(filename="result.mp4"):
  os.startfile(os.path.dirname(f"..\\app\\results\\{filename}.mp4"))

def assign_defaults():
    return "wav2lip", 1, "0 10 0 0", "result"


# ========================== GUI ==========================
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            # Empty column for centering the UI
            pass
        with gr.Column(scale=5): # ---------- Main column (centered) ------------------
            with gr.Row():
                gr.Markdown("# Talking Head Generator \n \
                            ### 1. Upload an image(.jpg, .jpeg, .png) or video(.mp4) <br/> \
                            2. Upload an audio(.mp3, .wav) file <br/> \
                            3. Generate a talking head which its lip movements are driven by the input audio (Lip-Synced Video). \n \
                            Tips: <br/> \
                            - By increasing bottom padding, you can include the chin for better results. <br/> \
                            - The wav2lip_gan model has better visual quality, but weaker LipSync accuracy. \
                            - Sometimes best results are obtained at 480p or 720p \
                            <br/><br/>")
            with gr.Row():
                gr.Markdown("# Input")
            with gr.Row():
                input_face = gr.File(label="Image/Video")
                input_audio = gr.File(label="Audio")
            with gr.Row():
                    with gr.Column(scale=1):
                        input_model_name = gr.Radio(label="Select a Model", choices=["wav2lip", "wav2lip_gan"], value="wav2lip",
                                                    interactive=True)
                    with gr.Column(scale=1):
                        input_resize_factor = gr.Slider(label="Resize Factor",
                                                        info="Reduces the resolution of the image/video",
                                                        value=1, minimum=1, maximum=10, step=1, interactive=True)
            with gr.Row():
                with gr.Column():
                    input_pads = gr.Textbox(label="Padding", info="(top, bottom, left, right)", value="0 10 0 0", interactive=True)
                with gr.Column():
                    output_filename = gr.Textbox(label="Output Filename", info="default: result", value="result")
            with gr.Row():
                btn_generate = gr.Button("Generate", variant="primary")
            with gr.Row():
                gr.Markdown("# Output")
            with gr.Row():
                with gr.Column(scale=4):
                    output_video = gr.Video(label="Video")
                with gr.Column(scale=1):
                    btn_show_in_folder = gr.Button("Show in Folder")
                    btn_clear = gr.ClearButton(value="Reset",
                                components=[input_face, input_audio, input_model_name, output_filename, output_video])
        with gr.Column(scale=2):
            # Empty column for centering the UI
            pass

    # ----------------- Functionalities ----------------------------
    btn_generate.click(fn=generate_video,
                       inputs=[input_face, input_audio, input_model_name, input_resize_factor, input_pads, output_filename],
                       outputs=[output_video])
    btn_show_in_folder.click(fn=show_folder, inputs=[output_filename], outputs=None)
    btn_clear.click(fn=assign_defaults, inputs=None,
                    outputs=[input_model_name, input_resize_factor, input_pads, output_filename])


demo.launch(share=True)

