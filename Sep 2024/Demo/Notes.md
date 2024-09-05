1. Image insert from css style file.
   1. since our temple is only html files not css files, so we can't use static tag inside css file.
   2. so for that we need to use relative path inside the url function of background-image property.
   3. for we are not using exteds tag.
2. Do you understand cache memory.
3. To Refresh your page use ctrl + F5. removing all cached css file and reload all css file from server.

Q: if we want to apply same bg-image on home-page instead of index page.	

1. extend index page by home_page.html template.
2. just reload the page and

Q: How to apply extends tag

1. create a place holder block (with a name) inside the parent template (index.html)
2. Create a child template (home_page.html)
3. create a block with same name created inside the parent template and put some content inside that.
4. put a `extends` tag inside the child template (`home_page.html`) for extending parent html template. ( `{% extends "index.html" %}`).
5. Chage your templage
