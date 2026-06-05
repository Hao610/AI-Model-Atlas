# LLaMA-Factory Training Guide 🛠️

[English] | [中文 (llama_factory_zh.md)](llama_factory_zh.md)

Writing PyTorch training loops, loss functions, and hardware tokenization from scratch is highly complex. 

To simplify this, the open-source community created **LLaMA-Factory**, a unified training dashboard. It provides a beautiful web interface where you can configure and fine-tune models using a simple click-and-run UI.

---

## 📅 Step 1: Prepare Your Training Data

LLaMA-Factory primarily uses the **Alpaca Format** (a JSON file containing a list of instruction/response pairs). 

Create a file named `my_data.json` with your training samples:

```json
[
  {
    "instruction": "Translate the following slang to medical terms.",
    "input": "My throat is scratchy and I feel hot.",
    "output": "Patient presents with mild pharyngitis and low-grade pyrexia."
  },
  {
    "instruction": "Translate the following slang to medical terms.",
    "input": "My belly is in knots.",
    "output": "Patient reports acute abdominal cramping."
  }
]
```

* **Instruction**: The command/prompt given to the model.
* **Input**: (Optional) Additional context or query data.
* **Output**: The ground-truth answer you want the model to learn.

---

## 🚀 Step 2: Install LLaMA-Factory

Open your terminal and run:

```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e .[metrics,bitsandbytes]
```

---

## 🖥️ Step 3: Launch the Web UI

Run the following command to start the local web dashboard:

```bash
llamafactory-cli webui
```

Open your browser and navigate to `http://localhost:7860`. You will see the LLaMA-Factory console:

```text
┌────────────────────────────────────────────────────────┐
│ LLaMA-Factory Webui                                     │
├────────────────────────────────────────────────────────┤
│ Model Name:   [ Llama-3-8B-Instruct ]                  │
│ Model Path:   [ /path/to/llama-3-8b ]                  │
│ Stage:        [ Supervised Fine-Tuning (SFT) ]         │
│ Adapter:      [ LoRA ]                                 │
├────────────────────────────────────────────────────────┤
│ Dataset:      [ my_data.json ]                         │
│ Learning Rate:[ 2e-4 ]       Epochs: [ 3.0 ]           │
│ LoRA Rank:    [ 8 ]          LoRA Alpha: [ 16 ]        │
├────────────────────────────────────────────────────────┤
│ [ Start Training ]  [ Preview Commands ]               │
└────────────────────────────────────────────────────────┘
```

---

## ⚙️ Step 4: Configuration Settings

Configure these parameters in the web interface:

1. **Model Name / Path**: Select your base model (e.g., Llama 3 or Qwen 2.5).
2. **Stage**: Set to **Supervised Fine-Tuning (SFT)**.
3. **Adapter**: Set to **LoRA**.
4. **Dataset**: Select your prepared `my_data.json` from the dropdown list.
5. **Hyperparameters**:
   * **Learning Rate**: Set to `2e-4` (Standard default).
   * **Epochs**: Set to `3` (The number of times the model will read your entire dataset).
   * **LoRA Rank (r)**: Set to `8` or `16`.
6. **Output Directory**: Define where the model will save your final `10MB` adapter files.

Click **Start** at the bottom of the page. LLaMA-Factory will print progress bars, loss charts, and training logs live! Once it reaches 100%, your LoRA adapter is ready to use.

---

Now that you know how to train a model, let's learn how to compress it so it can fit on cheaper hardware in [Model Quantization](quantization.md).
