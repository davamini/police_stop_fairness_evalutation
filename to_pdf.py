import os
import nbformat
from nbconvert import HTMLExporter


def convert_notebook(report_in_path, report_out_path, **kwargs):

    curdir = os.path.abspath(os.getcwd())
    indir, _ = os.path.split(os.path.join('dsc167_project', report_in_path))
    outdir, _ = os.path.split(os.path.join('dsc167_project', report_out_path))
    print(indir, _ )
    os.makedirs(outdir, exist_ok=True)

    config = {
        "ExecutePreprocessor": {"enabled": True},
        "TemplateExporter": {"exclude_output_prompt": True, "exclude_input": True, "exclude_input_prompt": True},
    }

    nb = nbformat.read(open(report_in_path), as_version=4)
    html_exporter = HTMLExporter(config=config)

    # change dir to notebook dir, to execute notebook
    os.chdir(indir)
    body, resources = (
        html_exporter
        .from_notebook_node(nb)
    )

    # change back to original directory
    os.chdir(curdir)

    with open(report_out_path, 'w') as fh:
        fh.write(body)
        
if __name__ == "__main__":
    convert_notebook(report_in_path = "sd_police_stop_report.ipynb", report_out_path= "cp_2.pdf")