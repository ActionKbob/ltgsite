!function(e){function t(e,t,r){e in s||(s[e]={name:e,declarative:!0,deps:t,declare:r,normalizedDeps:t})}function r(e){return d[e]||(d[e]={name:e,dependencies:[],exports:{},importers:[]})}function n(t){if(!t.module){var o=t.module=r(t.name),u=t.module.exports,i=t.declare.call(e,function(e,t){if(o.locked=!0,"object"==typeof e)for(var r in e)u[r]=e[r];else u[e]=t;for(var n=0,i=o.importers.length;i>n;n++){var a=o.importers[n];if(!a.locked)for(var s=0;s<a.dependencies.length;++s)a.dependencies[s]===o&&a.setters[s](u)}return o.locked=!1,t},t.name);o.setters=i.setters,o.execute=i.execute;for(var c=0,l=t.normalizedDeps.length;l>c;c++){var f,p=t.normalizedDeps[c],v=s[p],h=d[p];h?f=h.exports:v&&!v.declarative?f=v.esModule:v?(n(v),h=v.module,f=h.exports):f=a(p),h&&h.importers?(h.importers.push(o),o.dependencies.push(h)):o.dependencies.push(null),o.setters[c]&&o.setters[c](f)}}}function o(t){var r={};if(("object"==typeof t||"function"==typeof t)&&t!==e)if(l)for(var n in t)"default"!==n&&u(r,t,n);else{var o=t&&t.hasOwnProperty;for(var n in t)"default"===n||o&&!t.hasOwnProperty(n)||(r[n]=t[n])}return r.default=t,f(r,"__useDefault",{value:!0}),r}function u(e,t,r){try{var n;(n=Object.getOwnPropertyDescriptor(t,r))&&f(e,r,n)}catch(n){return e[r]=t[r],!1}}function i(t,r){var n=s[t];if(n&&!n.evaluated&&n.declarative){r.push(t);for(var o=0,u=n.normalizedDeps.length;u>o;o++){var l=n.normalizedDeps[o];-1==c.call(r,l)&&(s[l]?i(l,r):a(l))}n.evaluated||(n.evaluated=!0,n.module.execute.call(e))}}function a(e){if(v[e])return v[e];if("@node/"==e.substr(0,6))return v[e]=o(p(e.substr(6)));var t=s[e];if(!t)throw"Module "+e+" not present.";return n(s[e]),i(e,[]),s[e]=void 0,t.declarative&&f(t.module.exports,"__esModule",{value:!0}),v[e]=t.declarative?t.module.exports:t.esModule}var s={},c=Array.prototype.indexOf||function(e){for(var t=0,r=this.length;r>t;t++)if(this[t]===e)return t;return-1},l=!0;try{Object.getOwnPropertyDescriptor({a:0},"a")}catch(e){l=!1}var f;!function(){try{Object.defineProperty({},"a",{})&&(f=Object.defineProperty)}catch(e){f=function(e,t,r){try{e[t]=r.value||r.get.call(e)}catch(e){}}}}();var d={},p="undefined"!=typeof System&&System._nodeRequire||"undefined"!=typeof require&&require.resolve&&"undefined"!=typeof process&&require,v={"@empty":{}};return function(e,r,n,u){return function(i){i(function(i){for(var s=0;s<r.length;s++)!function(e,t){t&&t.__esModule?v[e]=t:v[e]=o(t)}(r[s],arguments[s]);u({register:t});var c=a(e[0]);if(e.length>1)for(var s=1;s<e.length;s++)a(e[s]);return n?c.default:c})}}}("undefined"!=typeof self?self:global)(["1"],[],!1,function(e){this.require,this.exports,this.module;e.register("2",[],function(e){"use strict";var t;return{setters:[],execute:function(){t=function(){var e=document.querySelectorAll(".collapse");[].forEach.call(e,function(e){e.querySelector(".collapse-toggle").addEventListener("click",function(t){e.querySelector(".collapse-content").classList.toggle("shown")})})}(),e("default",t)}}}),e.register("1",["2"],function(e){"use strict";var t;return{setters:[function(e){t=e.default}],execute:function(){}}})})(function(e){e()});
//# sourceMappingURL=main.bundle.js.map
