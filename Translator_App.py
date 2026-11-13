import tkinter as tk
from tkinter import ttk, messagebox

# OFFLINE DICTIONARY - Bina Internet Ke Chalega!
DATA = {
    ("English", "Urdu"): {
        "hello": "ہیلو",
        "how are you": "تم کیسے ہو؟",
        "good morning": "صبح بخیر",
        "good night": "شب بخیر",
        "thank you": "شکریہ",
        "i love you": "میں تم سے پیار کرتی ہوں",
        "what is your name": "تمہارا نام کیا ہے؟",
        "where are you": "تم کہاں ہو؟",
        "i am fine": "میں ٹھیک ہوں",
        "welcome": "خوش آمدید",
        "goodbye": "اللہ حافظ",
        "please help me": "براہ کرم میری مدد کریں",
        "i am hungry": "مجھے بھوک لگی ہے",
        "water": "پانی",
        "food": "کھانا",
        "friend": "دوست",
        "family": "خاندان",
        "love": "محبت",
        "school": "اسکول",
        "computer": "کمپیوٹر",
    },
    ("English", "Hindi"): {
        "hello": "नमस्ते",
        "how are you": "तुम कैसे हो?",
        "good morning": "सुप्रभात",
        "thank you": "धन्यवाद",
        "i love you": "मैं तुमसे प्यार करती हूँ",
        "welcome": "स्वागत है",
        "goodbye": "अलविदा",
        "water": "पानी",
        "food": "खाना",
        "friend": "दोस्त",
        "computer": "कंप्यूटर",
    },
    ("Urdu", "English"): {
        "ہیلو": "Hello",
        "شکریہ": "Thank You",
        "خوش آمدید": "Welcome",
        "اللہ حافظ": "Goodbye",
        "دوست": "Friend",
        "پانی": "Water",
    }
}

LANGS = ["English", "Urdu", "Hindi"]

def translate_text():
    text = input_box.get("1.0", tk.END).strip().lower()
    if not text:
        messagebox.showwarning("Warning", "Pehle kuch likho!")
        return
    frm = from_combo.get()
    to = to_combo.get()
    if frm == to:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, input_box.get("1.0", tk.END).strip())
        return
    dictionary = DATA.get((frm, to), {})
    # Word by word try karo
    if text in dictionary:
        result = dictionary[text]
    else:
        words = text.split()
        translated_words = []
        for w in words:
            translated_words.append(dictionary.get(w, f"[{w}]"))
        result = " ".join(translated_words)
        if "[" in result:
            result += "\n\n(Note: Ye Demo Dictionary hai - Full version me Google API se sab translate hoga)"
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)
    status_label.config(text="✅ Translated Successfully! (Offline Mode)")

def clear_all():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)
    status_label.config(text="Ready...")

def swap_lang():
    a = from_combo.get(); b = to_combo.get()
    from_combo.set(b); to_combo.set(a)

def copy_text():
    t = output_box.get("1.0", tk.END).strip()
    if t:
        root.clipboard_clear(); root.clipboard_append(t)
        status_label.config(text="✅ Copied!")

root = tk.Tk()
root.title("AI Translator App - Nisha - Offline")
root.geometry("700x620")
root.configure(bg="#1e3a8a")
tk.Label(root, text="🌍 AI TRANSLATOR APP", font=("Arial", 20, "bold"), bg="#1e3a8a", fg="white").pack(pady=10)
tk.Label(root, text="OFFLINE MODE - Bina Internet Ke Chalega!", font=("Arial", 11), bg="#1e3a8a", fg="#fde68a").pack()
frame = tk.Frame(root, bg="#1e3a8a"); frame.pack(pady=10)
from_combo = ttk.Combobox(frame, values=LANGS, font=("Arial", 12), width=15); from_combo.set("English"); from_combo.pack(side="left", padx=5)
tk.Button(frame, text="⇄ SWAP", command=swap_lang, bg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
to_combo = ttk.Combobox(frame, values=LANGS, font=("Arial", 12), width=15); to_combo.set("Urdu"); to_combo.pack(side="left", padx=5)
tk.Label(root, text="👇 Yahan Likho: (Example: hello / thank you / how are you)", bg="#1e3a8a", fg="white", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
input_box = tk.Text(root, height=4, font=("Arial", 13), bg="white"); input_box.pack(padx=20, fill="x")
btn_frame = tk.Frame(root, bg="#1e3a8a"); btn_frame.pack(pady=10)
tk.Button(btn_frame, text="🔍 TRANSLATE", command=translate_text, bg="#22c55e", fg="white", font=("Arial", 12, "bold"), width=15).pack(side="left", padx=5)
tk.Button(btn_frame, text="📋 COPY", command=copy_text, bg="#f59e0b", fg="white", font=("Arial", 12, "bold"), width=10).pack(side="left", padx=5)
tk.Button(btn_frame, text="🗑️ CLEAR", command=clear_all, bg="#ef4444", fg="white", font=("Arial", 12, "bold"), width=10).pack(side="left", padx=5)
tk.Label(root, text="✨ Translation:", bg="#1e3a8a", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
output_box = tk.Text(root, height=5, font=("Arial", 14), bg="#eff6ff"); output_box.pack(padx=20, fill="x")
status_label = tk.Label(root, text="Ready... Offline Mode", bg="#1e3a8a", fg="white", font=("Arial", 10)); status_label.pack(pady=10)
tk.Label(root, text="Try: hello | thank you | good morning | how are you", bg="#1e3a8a", fg="#bfdbfe", font=("Arial", 10)).pack()
tk.Label(root, text="Made by Nisha", bg="#1e3a8a", fg="#bfdbfe").pack()
root.mainloop()