import os


def save_table(filename: str, latex_code: str):
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    fullpath = f"{current_dir}/../latex_tables/{filename}.tex"
    fullpath = os.path.realpath(fullpath)
    with open(fullpath, 'w') as f:
        f.write(latex_code)

    print(f"Saved latex code to {filename}")


def save_plot(plt, filename: str, caption: str, label: str):
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    plot_dir = os.path.join(current_dir, "../plots/assets")
    latex_dir = os.path.join(current_dir, "../plots")

    plot_fullpath = os.path.realpath(os.path.join(plot_dir, f"{filename}.png"))
    latex_fullpath = os.path.realpath(os.path.join(latex_dir, f"{filename}.tex"))

    plt.savefig(plot_fullpath, dpi=300)

    latex_code = f"""
\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=\\textwidth]{{results/plots/assets/{filename}.png}}
    \\caption{{{caption}}}
    \\label{{{label}}}
\\end{{figure}}
    """.strip()

    with open(latex_fullpath, 'w') as f:
        f.write(latex_code)

    print(f"Saved plot to {filename}")
