!function(r,i){var t,o,s,e,c,d,a,l,u,n,f=".be1d8798",p=r.head,y="[native code]",m=[].indexOf;"function"==typeof m&&-1!==m.toString().indexOf(y)&&p&&(i.a2a=i.a2a||{},t=i.a2a_config=i.a2a_config||{},m=(o=r.currentScript)&&o.src?o.src:"",NodeList&&NodeList.prototype.forEach&&(i.a2a.init=function(e){t.linkurl&&r.querySelectorAll(".a2a_dd:not([data-a2a-url]):not(.a2a_target)").forEach(function(e){e.a2a_index||e.setAttribute("data-a2a-url",t.linkurl)})},i.a2a_init=i.a2a.init,t.linkurl&&o&&!o.async&&!o.defer&&i.a2a.init("page")),i.a2a.page||(i.a2a.page=!0,s=[],["init_all","svg_css"].forEach(function(a){i.a2a[a]=function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t];s.push([a,e])}}),n=(e=t.static_server)?e+"/":"https://static.addtoany.com/menu/",a=m&&-1!==m.split("/")[2].indexOf("addtoany"),c=(a=(c=!e&&a?m:n).match(/^[^?#]+\//))?a[0]:c,d=function(e,t,a){void 0===e&&(e=c+"eso"+f+".js"),void 0===t&&(t=!1);var n=r.createElement((a=void 0===a?!1:a)?"link":"script"),i="module",a=(a?(a="preload",n.href=e,n.rel=t?i+a:a,t||(n.as="script")):(n.src=e,t&&(n.type=i,n.onerror=function(){return d()})),o&&o.nonce?o.nonce:null);a&&(n.nonce=a),p.appendChild(n)},"function"==typeof(m="".matchAll)&&m.toString().includes(y)?(a=n+(e?"":"svg/"),d((m=c+(e?"":"modules/"))+"core"+f+".js",!0),y=document.createElement("link").relList.supports("modulepreload"),t.overlays&&t.overlays.length&&y&&d(m+"overlays"+f+".js",!0,!0),r.querySelector('.a2a_dd:empty,.a2a_kit [class*="a2a_button_"]:empty')&&d(a+"icons.30.svg.js",!1,!0)):d(),u=function(e){var t=i.a2a.core;"function"!=typeof t||e?e?e():i.a2a.core=function(e){return u(e)}:t()},n=function(){var e,t,a,n;t="a2a_menu_container",e=r.getElementById(t),i.a2a.main=l=e||r.createElement("div"),l.id!=t&&(l.style.position="static",r.body.insertBefore(l,null)),u(),s.forEach(function(e){var t;(t=i.a2a)[e[0]].apply(t,e[1])}),i.addEventListener("message",function(e){var t;".addtoany.com"===e.origin.substr(-13)&&"object"==typeof(e=e.data)&&e.a2a&&("function"==typeof(t=i.a2a.userServices)?t(e.user_services):i.a2a.userServices=e.user_services,r.getElementById("a2a_sm_ifr").style.display="none")}),e=r.createElement("iframe"),t=r.createElement("div"),a=e.style,n=t.style,e.id="a2a_sm_ifr",a.width=a.height=n.width=n.height="1px",a.top=a.left=a.border="0",a.position=n.position="absolute",a.zIndex=n.zIndex="100000",e.title="AddToAny Utility Frame",e.setAttribute("transparency","true"),e.setAttribute("allowTransparency","true"),e.setAttribute("frameBorder","0"),e.src="https://static.addtoany.com/menu/sm.23.html#type=core&event=load",n.top="0",n.visibility="hidden",l.insertBefore(t,null),t.insertBefore(e,null)},"loading"!==r.readyState?n():r.addEventListener("DOMContentLoaded",n)))}(document,window);