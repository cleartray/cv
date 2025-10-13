# CV Builder

## Running locally
Clone the repo with:
```shell
# If github CLI is available
gh repo clone cleartray/cv

# Otherwise
git clone git@github.com:cleartray/cv.git
```

Navigate to the newly-cloned directory
```shell
cd cv
```

Install Python dependencies with:
```shell
pip install -r requirements.txt
```

Place content in appropriate directories:
- CV Definition yaml in `input/cv_definitions`, see `example.yaml` for sample structure
- Input images for icons in `input/img`, square SVG icons are strongly recommended
- (Optional) any additional fonts in `input/font`
- (Optional) any additional styles in `input/css`
- (Optional) any additional HTML jinja templates in `input/html`

Then execute with:
```shell
python run.py
```

This should produce output PDFs in the `output` directory.
