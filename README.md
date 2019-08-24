# Markdown to Html Converter
Built from the ground up, a customizable program that converts [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax to HTML ready for website.  

## Usage
1. Takes in a Markdown file `.md` 
2. Returns `.html` file

## Capabilites
## Header Tags to \<h_>
<pre>
# H1
## H2
### H3
#### H4
</pre>

# H1
## H2
### H3
#### H4


## Lists to \<ol> | \<ul>
<pre>
1. First Order
2. Second Order
3. Third Order
4. Kylo
5. Hux

- Unordered One
- Unordered Two
* Unordered with asterisk
+ Unordered with plus
</pre>

1. First Order
2. Second Order
3. Third Order
4. Kylo
5. Hux

- Unordered One
- Unordered Two
* Unordered with asterisk
+ Unordered with plus


## Links to \<a href="">
<pre>
[Muh Link](https://xaviercollantes.com)
</pre>
[Muh Link](https://xaviercollantes.com)


## Images to \<img src="">
<pre>
![alt text](https://emojis.slackmojis.com/emojis/images/1493910338/2181/stormtrooper.png?1493910338)
</pre>

![alt text](https://emojis.slackmojis.com/emojis/images/1493910338/2181/stormtrooper.png?1493910338)


## Not Supported (TODO)
## Alt Header Tags
<pre>
H1-Alternative
==============
H2-Alternative
--------------
</pre>

H1-Alternative
==============
H2-Alternative
--------------

## Inline Bold, Italic, Strikethrough
<pre>
**Bold** or __Bold__
*Italic* or _Italic_
~~Strikethrough~~
</pre>


**Bold** or __Bold__
*Italic* or _Italic_
~~Strikethrough~~


## Reference Links
<pre>
[refering to below][reference]

[End of document reference links]:(https://reference.com)
</pre>


[refering to below][reference]

[End of document reference links]:(https://reference.com)


## Credits
[Adam's Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
