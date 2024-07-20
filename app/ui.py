import webbrowser
import gradio as gr
import os

# Gradio paths are paths to temporary files (copy of the original) which get deleted after the program is closed
# The files are located in the server where gradio app is running
def generate_video(face_path, audio_path, model_name, filename="result", ):
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
        --outfile {output_path}
        """

    return_code = os.system(command)
    if return_code == 0:
        print("\n======== The video was generated successfully ========\nVideo saved at: " + output_path)
        return output_path
    else:
        return "Error during video generation"

def show_video(filename="result.mp4"):
  os.startfile(os.path.dirname(f"..\\app\\results\\{filename}.mp4"))

def assign_defaults():
    return "wav2lip", "result"



# ========================== GUI ==========================
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            # Empty column for centering the UI
            pass
        with gr.Column(scale=5): # ---------- Main column (centered) ------------------
            with gr.Row():
                gr.Markdown("# Talking Head Generator \n \
                            ### 1. Upload an image(.jpg) or video(.mp4) <br/> \
                            2. Upload an audio(.mp3) file <br/> \
                            3. Get a video which its lip movements are driven by the audio in any language (Lip-Synced Video). \
                            <hr/>")
            with gr.Row():
                input_face = gr.File(label="Image/Video (.jpg, .mp4)")
                input_audio = gr.File(label="Audio (.mp3)")
            with gr.Row():
                input_model_name = gr.Radio(label="Select a Model", choices=["wav2lip", "wav2lip_gan"], value="wav2lip",
                                            interactive=True)
            with gr.Row():
                with gr.Column(scale=2):
                    output_filename = gr.Textbox(label="Output Filename (default: result)", value="result")
                with gr.Column(scale=1):
                    btn_generate = gr.Button("Generate", variant="primary")
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
    btn_generate.click(fn=generate_video, inputs=[input_face, input_audio, input_model_name, output_filename], outputs=[output_video])
    btn_show_in_folder.click(fn=show_video, inputs=[output_filename], outputs=None)
    btn_clear.click(fn=assign_defaults, inputs=None, outputs=[input_model_name, output_filename])


demo.launch(share=True)

