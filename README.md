# FixMalk

Note: This is now out of date; the issue this hack addresses has been resolved (really, I don't know why I didn't just contact them directly, other than the fun of the hack and then forgetting about it.  Next time).
[](http://drinkmalk.com/stanza/node/3214)
[](http://www.drinkmalk.com/stanza/node/3234)

[DrinkMalk](http://www.drinkmalk.com) is an eBook catalogue, however
the 2.0 release of the [Aldiko](http://www.aldiko.com) reader for
android is unable to downloads (you can still browse the catalogue).
This appears to be because drinkmalk produces output that doesn't
quite conform to [the spec](http://opds-spec.org/) (a missing `rel`
attribute).

This is a simple proxy that you can run locally and use as alternative
catalogue service; it simply forwards all requests to drinkmalk and
returns all responses, correcting where needed so that downloads work
again.

## Usage

FixMalk was developed under python 2.5 on OSX, but should work on any
platform and later version (and possibly earlier versions, I haven't
checked).  You will need fixmalk running on a machine on the same
wireless network that your phone is connected to.

Assuming you are going to run fixmalk on a machine with the IP address
`10.0.0.2`, create a new custom catalogue in Aldiko using the url
`http://10.0.0.2:8080/list.xml`, and run fixmalk.  You should then be
able to browse and download books through your fixmalk catalogue.

## Caveats

Drinkmalk itself comes with a warning that it is only intended to be used
to read electronic copies of books you already own; please heed this
and be aware that of course fixmalk doesn't circumvent it in any way.
