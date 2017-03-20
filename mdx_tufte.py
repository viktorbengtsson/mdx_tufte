"""
Python-Markdown extension that provides support for HTML output compatible with tufte.css
(see https://github.com/edwardtufte/tufte-css)
=========================================
The tufte.css "provides tools to style web articles using the ideas demonstrated by
Edward Tufte’s books and handouts". This extension provides support for Markdown patterns
that parse to the following components of tufte.css:

Margin notes

Side notes

Figures

Fullwidth figures


Usage:

"""


from __future__ import absolute_import
from __future__ import unicode_literals
import markdown
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.inlinepatterns import Pattern


TUFTE_RE = r'[!]{2}(?P<label>.+)[|](?P<text>.+)[!]{2}'

class TufteExtension(Extension):
    """ Extension class for markdown """

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns["tufte"] = TuftePattern(TUFTE_RE, md)


class TuftePattern(Pattern):

    def handleMatch(self, matched):

        """
        If string matched
        regexp expression create
        new span elem with given class
        """

        lbl = matched.group("label")
        text = matched.group("text")
        # alt = matched.group("alt")
        # src = matched.group("src")

        spanelem = markdown.util.etree.Element("span")
        spanelem.set("class", 'marginnote')
        spanelem.text = markdown.util.AtomicString(text)

        labelelem = markdown.util.etree.Element("label")
        labelelem.set("for", lbl)
        labelelem.set("class", 'margin-toggle')
        labelelem.text = markdown.util.AtomicString(u'&#8853;')
        inputelem = markdown.util.etree.Element("input")
        inputelem.set("type", 'checkbox')
        inputelem.set("id", lbl)
        inputelem.set("class", 'margin-toggle')

        spanelem.append(labelelem)
        spanelem.append(inputelem)

        return spanelem


def makeExtension(*args, **kwargs):
    return TufteExtension(*args, **kwargs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()