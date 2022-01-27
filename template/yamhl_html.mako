<%
    import pdoc
    import yamhl
%>

<!DOCTYPE html>
<html lang="en">

<head id="head">
    <link rel="stylesheet preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>
    <script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
    <%include file="head.mako"/>
</head>

<body>
    <div id="splash"></div>
    <main>
        <article id="content">
${content}
        </article>
        <nav id="sidebar">
        <%include file="logo.mako"/>
        <%include file="toc.mako"/>
        </nav>
    </main>
    <footer id="footer">
    <%include file="credits.mako"/>
    <p>Generated with
    <a href="https://yamhl.pages.dev" title="yamhl: Yet Another Markdown 2 HTML Library"><cite>yamhl</cite> ${yamhl.__version__}</a> and
    <a href="https://pdoc3.github.io/pdoc" title="pdoc: Python API documentation generator"><cite>pdoc</cite> ${pdoc.__version__}</a>.</p>
    </footer>
</body>

</html>