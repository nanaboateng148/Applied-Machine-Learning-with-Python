#!/usr/bin/env python
# coding: utf-8

# ### Build your book
# 
# - [jupiter book website](https://jupyterbook.org/en/stable/intro.html)
# 
# - [my deployed book page ](https://nanaboateng148.github.io/Applied-Machine-Learning-with-Python)
# 
# https://nanaboateng148.github.io/Applied-Machine-Learning-with-Python
# 
# 
# Once you’ve added content and configured your book, it’s time to build outputs for your book. We’ll use the jupyter-book build command line tool for this.
# 
# Currently, there are two kinds of supported outputs: an HTML website for your book, and a PDF that contains all of the pages of your book that is built from the book HTML. In this tutorial, we’ll focus on building HTML outputs.
# 
# ### Prerequisites
# In order to build the HTML for each page, you should have followed the steps in Overview and Create a template book. You should have a collection of notebook/Markdown files in your mybookname/ folder, a `_toc.yml` file that defines the structure of your book, and any configuration you’d like in the` _config.yml` file.
# 
# ### Build your book’s HTML
# Now that your book’s content is in your book folder and you’ve defined your book’s structure in _toc.yml, you can build the HTML for your book.
# 
# Do so by running the following command:
# 
# `jupyter-book build --all mybookname/`
# 
# jupyter-book build mybookname/
# This will generate a fully-functioning HTML site using a static site generator. The site will be placed in the _build/html folder, something like this:
# 
# ```mybookname
#  └──_build
#     └── html
#        ├── _images
#        ├── _static
#        ├── index.html
#        ├── intro.html
#        ...
#        ```
# 
# 
# These are the static files for a standalone website! They contain the HTML and all assets needed to view your book in a browser.
# 
# You can open the pages in the site by navigating to that folder and opening the html files with your web browser.
# 
# Note
# 
# You can also use the short-hand jb for jupyter-book. E.g.,: jb build mybookname/.
# 
# Aside: Source vs build files
# At this point, you have created a combination of Jupyter notebooks, markdown files, and configuration files, including _toc.yml and _config.yml. These files are your source files. The source files comprise all of the content and configuration that Jupyter Book needs to build your book.
# 
# In addition, you have created a collection of outputs in the _build folder. The _build folder contains all of your static website build files. The build files contain all of the output from Jupyter Book’s build command. These files are only used to view your content in a browser or to share with others.
# 
# The best practice for publishing your book is to use separate branches for your source and your build files. For example, you may tell git to ignore your _build folder on your main branch, and push the outputs in your _build folder to a branch called gh-pages. We’ll cover some of this later on.
# 
# A note on page cacheing
# 
# By default, Jupyter Book will only build the HTML for pages that have been updated since the last time you built the book.
# 
# If you’d like to force Jupyter Book to re-build a particular page, you can either edit the corresponding file in your book’s folder, or delete that page’s HTML in the _build/html folder.
# 
# You can also signal a full re-build using the --all option:
# 
# `jupyter-book build --all mybookname/`
# 
# ### Preview your built HTML
# To preview your book, you can open the generated HTML files in your browser. Either double-click the html file in your local folder, or enter the absolute path to the file in your browser navigation bar adding file:// at the beginning (e.g. file://Users/my_path_to_book/_build/index.html).
# 
# Take a look at the web page that was generated from the markdown page that you created. Note how the links you inserted were automatically resolved to point to the right place. This is how you can keep consistent pointers from one section of your book to another.
# 
# ### Create your own content
# Now that you’ve built a simple HTML site from your demo book, we’ll create some new content so that you can get the hang of adding new files. See Create your own content file for the next step.
# 
# 
# 
# Create your own content file
# Now that you’ve seen a few sample content files, and built a simple book, try creating your own!
# 
# Create your file and add content to it
# In the folder with all of your sample book contents, create a new file called mymarkdownfile.md. Put the following content in it:
# 
# ### Here's my sample title
# 
# This is some sample text.
# 
# `(section-label)=`
# 
# ### Here's my first section
# 
# Here is a `[reference to the intro](intro.md)`. Here is a reference to `[](section-label)`.
# We’ve added two new pieces of markdown syntax, both of them are related to cross-references.
# 
# `(section-label)=` is a label that’s attached to a section header. It refers to whatever header follows, and allows you to refer to this label later on in your text.
# 
# `[link text](link-target)` syntax is how you specify a link in markdown. Here we’ve linked to another page, as well as to the label we created above.
# 
# When you build your book, you’ll see how these links resolve in the output.
# 
# Add it to your Table of Contents
# Now that you’ve got a new file, we need to add it to your _toc.yml file so that Jupyter Book knows where it fits with your book’s structure. Add the a line to your _toc.yml file pointing to this new content, it should look something like this:
# 
# ### In _toc.yml
# 
# `format: jb-book
# root: intro
# chapters:
# - file: markdown
# - file: notebooks
# - file: markdown-notebooks
# - file: mymarkdownfile`
# 
# Re-build your book
# Now that you’ve added the file to your _toc.yml file, you can re-run the build command:
# 
# `jupyter-book build mybookname`
# 
# This will re-build your book, and your new page will show up in the output.
# 
# 
# 
# ### Publish your book online
# 
# Once you’ve built the HTML for your book, you can host it online. The best way to do this is with a service that hosts static websites (because that’s what you have just created with Jupyter Book). In this tutorial, we’ll cover how to publish your book online with GitHub Pages, a popular and free online hosting platform.
# 
# ###Create an online repository for your book
# 
# In order to connect your hosted book with your book’s source content, you should put your book’s source content in a public repository. This section describes one approach to create your own GitHub repository and add your book’s content to it.
# 
# 1. First, log in to GitHub, then go to the “create a new repository” page: https://github.com/new
# 
# 2. Next, give your online repository a name and a description. Make your repository public and do not initialize it with a README file, then click “Create repository”.
# 
# 3. Now, clone the (currently empty) online repository to a location on your local computer. You can do this via the command line with:
# 
# `git clone https://github.com/<my-org>/<my-repository-name>`
#     
# Copy all of your book files and folders into this newly cloned repository. For example, if you created your book locally with jupyter-book create mylocalbook and your new repository is called myonlinebook, you could do this via the command line with:
# 
# `cp -r mylocalbook/* myonlinebook/`
#     
# Now you need to sync your local and remote (i.e., online) repositories. You can do this with the following commands:
# 
# `cd myonlinebook
# git add ./*
# git commit -m "adding my first book!"
# git push`
#     
# ### Publish your book online with GitHub Pages
# We have just pushed the source files for our book into our GitHub repository. This makes it publicly accessible for you or others to see.
# 
# Next, we’ll publish the build artifact of our book online, so that it is rendered as a website.
# 
# The easiest way to use GitHub Pages with your built HTML is to use the ghp-import package. ghp-import is a lightweight Python package that makes it easy to push HTML content to a GitHub repository.
# 
# ghp-import works by copying all of the contents of your built book (i.e., the _build/html folder) to a branch of your repository called gh-pages, and pushes it to GitHub. The gh-pages branch will be created and populated automatically for you by ghp-import. To use ghp-import to host your book online with GitHub Pages follow the steps below:
# 
# Note
# 
# Before performing the below steps, ensure that HTML has been built for each page of your book (see the previous section). There should be a collection of HTML files in your book’s ` _build/html folder`.
# 
# 1. `Install ghp-import`
# 
# `pip install ghp-import`
#     
# 2. Update the settings for your GitHub pages site:
# 
# a. Use the gh-pages branch to host your website.
# 
# b. Choose root directory / if you’re building the book in it’s own repository. Choose /docs directory if you’re building documentation with jupyter-book.
# 
# 3. From the main branch of your book’s root directory (which should contain the `_build/html` folder) call ghp-import and point it to your HTML files, like so:
# 
# `ghp-import -n -p -f _build/html`
# 
# Warning
# 
# Make sure that you included the -n - this tells GitHub not to build your book with Jekyll, which we don’t want because our HTML is already built! If you do not do this you may see 404 not found for your deployed content.
# 
# Typically after a few minutes your site should be viewable online at a url such as: `https://<user>.github.io/<myonlinebook>/`. If not, check your repository settings under Options -> GitHub Pages to ensure that the gh-pages branch is configured as the build source for GitHub Pages and/or to find the url address GitHub is building for you.
# 
# To update your online book, make changes to your book’s content on the main branch of your repository, re-build your book with `jupyter-book build mybookname/` and then use `ghp-import -n -p -f mylocalbook/_build/html` as before to push the newly built HTML to the gh-pages branch.
# 
# Warning
# 
# Note this warning from the ghp-import GitHub repository:
# 
# “…ghp-import will DESTROY your gh-pages branch… and assumes that the gh-pages branch is 100% derivative. You should never edit files in your gh-pages branch by hand if you’re using this script…”
# 
# 
# 
# 
# ### Build a small example project
# Now that you’ve built your first book, you may wish to get some inspiration from a more “complete” book example.
# 
# This section describes the QuantEcom mini book to show you how it’s made.
# 
# Some of the features on display include
# 
# Jupyter Notebook-style inputs and outputs
# 
# citations
# 
# numbered equations
# 
# numbered figures with captions and cross-referencing
# 
# See also
# 
# For more inspiration and example books, see the Jupyter Book gallery
# 
# ### Mini-book source files
# The source files can be found on GitHub in the docs directory. These files are written in MyST Markdown, an extension of the Jupyter Notebook Markdown, that allows for additional scientific markup. They could alternatively have been written directly as Jupyter notebooks.
# 
# ### Build the demo book
# You can build this book locally on the command line via the following steps:
# 
# Ensure you have a recent version of Anaconda Python installed.
# 
# Clone the repository containing the demo book source files
# 
# ```git clone https://github.com/executablebooks/quantecon-mini-example
# cd quantecon-mini-example```
# 
# If you’d like to install Jupyter Book with pip, you can do so with:
# 
# ```pip install -U jupyter-book```
# See the getting started page for more information.
# 
# Install the Python libraries needed to run the code in this particular example from the environment.yml file. This includes the latest version of Jupyter Book:
# 
# ```conda env create -f environment.yml
# conda activate qe-mini-example```
# 
# Run Jupyter Book over the source files
# 
# jupyter-book build ./mini_book
# View the result through a browser — try (with, say, firefox)
# 
# firefox mini_book/_build/html/index.html
# (or simply double-click on the html file)
# 
# Now you might like to try editing the files in mini_book/docs and then rebuilding.
# 
# Further reading
# See the full QuantEcon example for a longer Jupyter Book use case, drawn from the same source material.

# In[ ]:





# In[ ]:




