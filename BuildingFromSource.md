# Details #

To build the Snake Wrangling for Kids PDF files from the LaTeX source, first checkout the source from the Mercurial repository.
Unzip all the image zip files.  If you're running Linux or Mac, you can use the following command:

```
for x in `ls -1 *.zip`; do unzip $x; done
```

After you've unzipped all the images, run the following command:

```
python setup.py build
```

After a few minutes, the PDF files for Linux, Windows and Mac will be generated in the `target` directory.