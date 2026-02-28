import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk, simpledialog
import platform
import subprocess
import time
import random
import os
import sys
import io
import contextlib
import ctypes

# =========================================================
# ALGORITHM: Cat OS In-Memory Virtual File System (VFS)
# =========================================================
class CatVFS:
    """A high-performance in-memory hierarchical file management system."""
    def __init__(self):
        # Initial memory state tree - branded for Cat OS
        self.memory_tree = {
            "ROOT:": {
                "System": {
                    "kernel.cat": "HEX_0x7FFA_CAT_CORE_v1.0",
                    "ui_config.json": "{\"theme\": \"Stark_HUD\", \"access\": \"Level_5\"}"
                },
                "Neural_Links": {
                    "User_Alpha": {
                        "manifesto.txt": "Welcome to Cat OS 1.X.\nReality is just data waiting to be processed.",
                    },
                    "Archive": {}
                }
            }
        }

    def _traverse(self, path):
        parts = [p for p in path.split("/") if p and p != "ROOT:"]
        current_node = self.memory_tree["ROOT:"]
        for part in parts:
            if part in current_node and isinstance(current_node, dict):
                current_node = current_node[part]
            else:
                return None
        return current_node

    def list_contents(self, path):
        node = self._traverse(path)
        return list(node.keys()) if isinstance(node, dict) else []

    def is_directory(self, path, name):
        node = self._traverse(path)
        if isinstance(node, dict) and name in node:
            return isinstance(node[name], dict)
        return False

    def write_file(self, path, filename, content):
        node = self._traverse(path)
        if isinstance(node, dict):
            if filename not in node or not isinstance(node[filename], dict):
                node[filename] = content
                return True
        return False

    def read_file(self, path, filename):
        node = self._traverse(path)
        if isinstance(node, dict) and filename in node:
            if not isinstance(node[filename], dict):
                return node[filename]
        return None

    def delete_item(self, path, name):
        node = self._traverse(path)
        if isinstance(node, dict) and name in node:
            del node[name]
            return True
        return False

# =========================================================
# CORE OS ENGINE: Cat OS 1.X (Stark HUD)
# =========================================================
class CatOS:
    def __init__(self, root):
        self.root = root
        self.root.title("CAT OS 1.X // NEURAL INTERFACE")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Stark OS HUD Color Palette
        self.bg_deep = "#020617"      # Deep Space Blue
        self.bg_panel = "#0F172A"     # Panel Slate
        self.cyan = "#22D3EE"         # Cyber Cyan
        self.indigo = "#818CF8"       # HUD Indigo
        self.pink = "#F472B6"         # Alert Pink
        self.text_dim = "#94A3B8"     # Ghost Text
        
        self.root.configure(bg="black")
        self.host_os = platform.system()
        self.vfs = CatVFS() 
        
        self.init_boot_sequence()

    def init_boot_sequence(self):
        """HUD-style boot sequence simulation."""
        self.boot_frame = tk.Frame(self.root, bg="black")
        self.boot_frame.pack(fill=tk.BOTH, expand=True)

        self.boot_log = tk.Text(self.boot_frame, bg="black", fg=self.cyan, 
                                font=("Consolas", 10), bd=0, highlightthickness=0)
        self.boot_log.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

        steps = [
            (">> INITIALIZING CAT OS 1.X [STARK CORE]", 400),
            (">> SCANNING HARDWARE TOPOLOGY...", 300),
            (f">> DETECTED HOST: {self.host_os.upper()}", 200),
            (">> ESTABLISHING NEURAL LINK...", 600),
            (">> [OK] SYNCING MEMORY RECURSION...", 200),
            (">> [OK] MOUNTING VFS (RAM_ONLY)...", 300),
            (">> [OK] DEPLOYING STARK HUD OVERLAY...", 400),
            (">> SYSTEM READY. WELCOME, OPERATOR.", 800)
        ]

        def process_boot(idx):
            if idx < len(steps):
                msg, delay = steps[idx]
                self.boot_log.insert(tk.END, msg + "\n")
                self.boot_log.see(tk.END)
                self.root.after(delay, lambda: process_boot(idx + 1))
            else:
                self.root.after(500, self.launch_desktop)

        process_boot(0)

    def launch_desktop(self):
        self.boot_frame.destroy()
        self.root.configure(bg=self.bg_deep)
        
        # Draw HUD Lines
        self.canvas = tk.Canvas(self.root, bg=self.bg_deep, highlightthickness=0)
        self.canvas.place(x=0, y=0, width=800, height=600)
        self.draw_hud_decorations()

        self.setup_ui_layers()

    def draw_hud_decorations(self):
        # Top Header Bar
        self.canvas.create_rectangle(0, 0, 800, 40, fill=self.bg_panel, outline=self.cyan)
        self.canvas.create_text(20, 20, text="CAT OS 1.X // SYSTEM STATUS: NOMINAL", 
                                fill=self.cyan, font=("Consolas", 10, "bold"), anchor="w")
        
        # Bottom Taskbar Area
        self.canvas.create_rectangle(0, 560, 800, 600, fill=self.bg_panel, outline=self.cyan)
        
        # Decorative HUD Corners
        self.canvas.create_line(10, 50, 50, 50, fill=self.cyan, width=2)
        self.canvas.create_line(10, 50, 10, 90, fill=self.cyan, width=2)
        
        self.canvas.create_line(750, 50, 790, 50, fill=self.cyan, width=2)
        self.canvas.create_line(790, 50, 790, 90, fill=self.cyan, width=2)

    def setup_ui_layers(self):
        self.main_container = tk.Frame(self.root, bg=self.bg_deep)
        self.main_container.place(x=50, y=60, width=700, height=480)

        # Icon Grid
        self.create_hud_icon("🧠\nASM_EXEC", 0, 0, self.open_asm_engine)
        self.create_hud_icon("📁\nVFS_CORE", 0, 1, self.open_vfs_explorer)
        self.create_hud_icon("⚡\nCOMPILER", 0, 2, self.open_compiler)
        self.create_hud_icon("🤖\nBYTEBOT", 1, 0, self.open_bytebot)
        self.create_hud_icon("⚙️\nHOST_APP", 1, 1, self.open_host_bridge)
        self.create_hud_icon("🛰️\nTERMINAL", 1, 2, self.open_cat_terminal)
        
        # Clock
        self.clock_lbl = tk.Label(self.root, text="", bg=self.bg_panel, fg=self.cyan, font=("Consolas", 12))
        self.clock_lbl.place(x=680, y=570)
        self.update_clock()

    def update_clock(self):
        self.clock_lbl.config(text=time.strftime("%H:%M:%S UTC"))
        self.root.after(1000, self.update_clock)

    def create_hud_icon(self, label, row, col, cmd):
        frame = tk.Frame(self.main_container, bg=self.bg_deep, bd=1, highlightbackground=self.indigo, highlightthickness=1)
        frame.grid(row=row, column=col, padx=20, pady=20)
        
        btn = tk.Button(frame, text=label, bg=self.bg_panel, fg=self.cyan, 
                        font=("Consolas", 9, "bold"), relief=tk.FLAT, width=15, height=5,
                        activebackground=self.cyan, activeforeground="black", command=cmd)
        btn.pack()

    # ---------------------------------------------------------
    # FEATURE: ASM ENGINE (Direct Memory Ops)
    # ---------------------------------------------------------
    def open_asm_engine(self):
        win = self.create_hud_window("NATIVE ASM ENGINE", 500, 450)
        
        tk.Label(win, text="[RAW HEX INJECTION]", bg=self.bg_panel, fg=self.pink, font=("Consolas", 10)).pack(pady=5)
        
        code_in = scrolledtext.ScrolledText(win, bg="black", fg=self.cyan, font=("Consolas", 10), height=6)
        code_in.pack(fill=tk.X, padx=10, pady=5)
        code_in.insert(tk.END, "b8 2a 00 00 00 c3  # mov eax, 42; ret")

        log = scrolledtext.ScrolledText(win, bg="black", fg=self.text_dim, font=("Consolas", 9), height=10)
        log.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        def run_asm():
            hex_data = code_in.get("1.0", tk.END).split("#")[0].strip().replace(" ", "")
            log.insert(tk.END, f">> Allocating HUD buffer for {len(hex_data)//2} bytes...\n")
            try:
                shellcode = bytes.fromhex(hex_data)
                if platform.system() == "Windows":
                    kernel32 = ctypes.windll.kernel32
                    ptr = kernel32.VirtualAlloc(0, len(shellcode), 0x3000, 0x40)
                    buf = (ctypes.c_char * len(shellcode)).from_buffer_copy(shellcode)
                    kernel32.RtlMoveMemory(ptr, buf, len(shellcode))
                    res = ctypes.CFUNCTYPE(ctypes.c_int)(ptr)()
                    log.insert(tk.END, f">> EAX RESULT: {res}\n")
                else:
                    log.insert(tk.END, ">> OS Security level prevents direct ASM on non-Win host.\n")
            except Exception as e:
                log.insert(tk.END, f">> SEGFAULT: {e}\n")

        tk.Button(win, text="EXECUTE PULSE", bg=self.cyan, fg="black", command=run_asm).pack(pady=5)

    # ---------------------------------------------------------
    # FEATURE: BYTEBOT ALGO GENERATOR
    # ---------------------------------------------------------
    def open_bytebot(self):
        win = self.create_hud_window("BYTEBOT ALGORITHM RUNTIME", 600, 500)
        
        tk.Label(win, text="INPUT OBJECTIVE:", bg=self.bg_panel, fg=self.cyan).pack(anchor="w", padx=10)
        prompt = tk.Entry(win, bg="black", fg=self.cyan, insertbackground=self.cyan)
        prompt.pack(fill=tk.X, padx=10, pady=5)
        prompt.insert(0, "Quick Sort Algorithm")

        code_view = scrolledtext.ScrolledText(win, bg="black", fg=self.indigo, font=("Consolas", 10), height=12)
        code_view.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        def generate():
            p = prompt.get().lower()
            if "sort" in p:
                c = "def sort(a):\n  if len(a)<=1: return a\n  p=a[0]\n  return sort([x for x in a[1:] if x<p])+[p]+sort([x for x in a[1:] if x>=p])\n\ndata=[9,3,7,1,5]\nprint(f'Input: {data}')\nprint(f'Sorted: {sort(data)}')"
            elif "prime" in p:
                c = "def is_prime(n):\n  return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))\n\nprint([x for x in range(50) if is_prime(x)])"
            else:
                c = "print('Cat OS: Objective identified but no template match.')"
            
            code_view.delete("1.0", tk.END)
            code_view.insert(tk.END, c)

        def execute():
            src = code_view.get("1.0", tk.END)
            out = io.StringIO()
            try:
                with contextlib.redirect_stdout(out):
                    exec(compile(src, '<bytebot>', 'exec'))
                messagebox.showinfo("Execution Results", out.getvalue())
            except Exception as e:
                messagebox.showerror("Runtime Error", str(e))

        btn_f = tk.Frame(win, bg=self.bg_panel)
        btn_f.pack(pady=5)
        tk.Button(btn_f, text="GENERATE", bg=self.indigo, fg="white", command=generate).pack(side="left", padx=5)
        tk.Button(btn_f, text="RUN IN RAM", bg=self.cyan, fg="black", command=execute).pack(side="left", padx=5)

    # ---------------------------------------------------------
    # UTILS: STARK WINDOW FACTORY
    # ---------------------------------------------------------
    def create_hud_window(self, title, w, h):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry(f"{w}x{h}")
        win.configure(bg=self.bg_panel)
        
        # Header Decor
        header = tk.Frame(win, bg=self.cyan, height=2)
        header.pack(fill=tk.X)
        
        title_lbl = tk.Label(win, text=f"// {title}", bg=self.bg_panel, fg=self.cyan, font=("Consolas", 10, "bold"))
        title_lbl.pack(pady=5)
        
        return win

    def open_vfs_explorer(self):
        win = self.create_hud_window("VFS EXPLORER", 400, 400)
        curr_path = tk.StringVar(value="/ROOT:")
        
        listbox = tk.Listbox(win, bg="black", fg=self.cyan, font=("Consolas", 10), bd=0)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        def refresh():
            listbox.delete(0, tk.END)
            for item in self.vfs.list_contents(curr_path.get()):
                p = "[DIR] " if self.vfs.is_directory(curr_path.get(), item) else "[FIL] "
                listbox.insert(tk.END, p + item)

        tk.Button(win, text="REFRESH PATH", command=refresh, bg=self.indigo, fg="white").pack(pady=5)
        refresh()

    def open_compiler(self):
        win = self.create_hud_window("MEM-SAFE COMPILER", 500, 400)
        code = scrolledtext.ScrolledText(win, bg="black", fg="#ADFF2F", font=("Consolas", 10))
        code.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        code.insert(tk.END, "import math\n# Compute Fibonacci in RAM\nphi = (1 + math.sqrt(5)) / 2\n[int((phi**n - (-1/phi)**n) / math.sqrt(5)) for n in range(10)]")
        
        def run():
            try:
                res = eval(code.get("1.0", tk.END))
                messagebox.showinfo("Memory Dump", f"Output: {res}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(win, text="COMPILE & EVAL", command=run, bg=self.cyan, fg="black").pack(pady=5)

    def open_host_bridge(self):
        win = self.create_hud_window("HOST BRIDGE", 300, 200)
        tk.Label(win, text=f"INTERFACE: {self.host_os}", bg=self.bg_panel, fg=self.text_dim).pack(pady=10)
        
        def launch(name):
            try:
                if self.host_os == "Windows": subprocess.Popen(f"{name}.exe")
                else: messagebox.showwarning("Bridge", "Host bridge optimized for x64 Windows.")
            except: pass

        tk.Button(win, text="OS_CALC", width=15, command=lambda: launch("calc")).pack(pady=2)
        tk.Button(win, text="OS_TERM", width=15, command=lambda: launch("cmd")).pack(pady=2)

    def open_cat_terminal(self):
        win = self.create_hud_window("CAT_OS TERMINAL", 500, 300)
        term = scrolledtext.ScrolledText(win, bg="black", fg=self.cyan, font=("Consolas", 10), insertbackground=self.cyan)
        term.pack(fill=tk.BOTH, expand=True)
        term.insert(tk.END, "CAT OS 1.X SHELL // READY\n>> ")

        def on_enter(e):
            lines = term.get("1.0", tk.END).split("\n")
            cmd = lines[-2].replace(">> ", "").strip()
            if cmd == "help": term.insert(tk.END, "Commands: clear, sys, vfs, exit\n")
            elif cmd == "sys": term.insert(tk.END, f"CAT_CORE_v1.0 // {self.host_os}\n")
            elif cmd == "clear": term.delete("1.0", tk.END)
            term.insert(tk.END, ">> ")
            term.see(tk.END)
            return "break"

        term.bind("<Return>", on_enter)

if __name__ == "__main__":
    root = tk.Tk()
    # Simple check for scaling on high-res displays
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    app = CatOS(root)
    root.mainloop()
