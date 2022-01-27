<%
    from yamhl.yamhl import YAMHL
    from yamhl.utils import ddir
%>
<div id="logo-div">
    <div><img src="/assets/images/icons/logo.png" class="logo"></div>
    <div><a href="/"><h1>${ddir(YAMHL, "md_vars/files/README/title")}</h1></a></div>
</div>