# llm_handler.py

from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llava15ChatHandler

class LlamaHandler:
    def __init__(self, model_path: str, clip_model_path: str):
        self.model_path = model_path
        self.clip_model_path = clip_model_path
        self.llm = None
        self._load_model()

    def _load_model(self):
        try:
            print(f"Loading model: {self.model_path}")
            chat_handler = Llava15ChatHandler(clip_model_path=self.clip_model_path)
            self.llm = Llama(
                model_path=self.model_path,
                chat_handler=chat_handler,
                n_ctx=2048,
                logits_all=True,   # required for LLaVA
                n_gpu_layers=-1,
                verbose=True
            )
        except Exception as e:
            print(f"Model loading failed: {e}")
            raise

    def create_chat_completion(self, user_prompt: str, image_data_uri: str, max_tokens: int = 128) -> str:
        try:
            response = self.llm.create_chat_completion(
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "image_url", "image_url": {"url": image_data_uri}},
                            {"type": "text", "text": user_prompt}
                        ],
                    }
                ],
                max_tokens=max_tokens
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Inference error: {e}")
            return ""