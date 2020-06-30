# Information for developers

This site uses a github action `.github/workflows/publish.yml` to take the rows of markdown table in `README.md` and combine them with the template file `template/index.html.erb` to create `index.html`.

The `index.html` file is then force-pushed to the `gh-pages` branch of the repository. This is set as the branch to publish via GitHub Pages in the [repo settings](https://github.com/ministryofjustice/acronyms/settings)
