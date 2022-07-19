# Todo

  * Add exclusions to copier.yaml
  * is filter_types.py still needed?
  * docs\doxygen\Doxyfile - template the following

```
PROJECT_NAME           = "template-project"
INPUT                  = ../../template-project
```

New plan - setup docusaurus templates for docs / blog
while working on sveltepress2






So for building the docs as an option
1. First method is to parse all the markdown except for the api directory via docusaurus, and let sphinx parse the api subdir
2. Second method is to parse all the markdown via sphinx for outputs such as man pages etc or non html formats


1. Doxygen xml generated
2. Input markdown file which specifies a class, ideally from /docs/content/api
3. Sphinx then parses this using Brethe to output some content
4. Also we may be able use "exhale" for tree views of the api
5. Sphinx can output in different formats using builder extensions

At this stage we now need to output or get to a format that can be imported into Docusarus
maybe markdown?

One option might be

RST Output
https://github.com/sphinx-contrib/restbuilder
followed by pandoc for rst to md?
https://stackoverflow.com/questions/45633709/how-to-convert-rst-files-to-md

This might work better
https://github.com/clayrisser/sphinx-markdown-builder
