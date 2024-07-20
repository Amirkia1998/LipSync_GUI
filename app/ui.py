import webbrowser
import gradio as gr
import os

# Gradio paths are paths to temporary files (copy of the original) which get deleted after the program is closed
# The files are located in the server where gradio app is running
def generate_video(face_path, audio_path, output_filename="result", model_name="wav2lip"):
    current_dir = os.getcwd()
    os.chdir("..\\wav2Lip")

    inference_script = "inference.py"
    model_path = f"checkpoints\\{model_name}.pth"
    output_path = f"..\\app\\results\\{output_filename}.mp4"

    command = f"""
        python {inference_script} \
        --checkpoint_path {model_path} \
        --face {face_path} \
        --audio {audio_path} \
        --outfile {output_path}
        """

    return_code = os.system(command)
    if return_code == 0:
        print("\n===== The video was generated successfully =====\nVideo saved at: " + output_path)
        return output_path
    else:
        return "Error during video generation"

def show_video(filename="result.mp4"):
  os.startfile(os.path.dirname(f"..\\app\\results\\{filename}.mp4"))


# ========================== GUI ==========================
with gr.Blocks() as demo:
    gr.Markdown("# Talking Head Generator")
    gr.Markdown("### 1. Upload an image(.jpg) or video(.mp4) <br/> 2. Upload an audio(.mp3) file <br/> \
                3. Get a video which its lip movements are driven by the audio in any language (Lip-Synced Video).")
    with gr.Row():
        input_face = gr.File(label="Image/Video (.jpg, .mp4)")
        input_audio = gr.File(label="Audio (.mp3)")
    with gr.Row():
        input_model_name = gr.Radio(label="Select a Model", choices=["wav2lip", "wav2lip_gan"], value="wav2lip", interactive=True)
    with gr.Row():
        with gr.Column(scale=5):
            output_filename = gr.Textbox(label="Output Filename (default: result)", value="result")
        with gr.Column(scale=2):
            btn_generate = gr.Button("Generate")
        with gr.Column(scale=2):
            btn_show_in_folder = gr.Button("Show in Folder")

    output_video = gr.Video(label="Video", width="30vw")


    btn_generate.click(fn=generate_video, inputs=[input_face, input_audio, output_filename], outputs=[output_video])
    btn_show_in_folder.click(fn=show_video, inputs=[output_filename], outputs=None)

demo.launch(share=True)

