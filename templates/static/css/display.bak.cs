body {  
 font: normal 11px auto Microsoft YaHei UI, Arial;
 color: #4f6b72;  
 background: aliceblue;
}  
a {  
 color: #c75f3e;  
}  
#mytable {  
 width: 700px;  
 padding: 0;  
 margin: 0;  
}  
caption {  
 padding: 0 0 5px 0;  
 width: 700px;   
 font: italic 16px Microsoft YaHei UI, Arial;
 text-align: right;  
}  
th {  
 font: bold 16px Arial;
 color: #4f6b72;  
 border-right: 1px solid #C1DAD7;  
 border-bottom: 1px solid #C1DAD7;  
 border-top: 1px solid #C1DAD7;  
 letter-spacing: 2px;  
 text-transform: uppercase;  
 text-align: left;  
 padding: 6px 6px 6px 12px;  
 background: #CAE8EA url(images/bg_header.jpg) no-repeat;  
}  
th.nobg {  
 border-top: 0;  
 border-left: 0;  
 border-right: 1px solid #C1DAD7;  
 background: none;  
}  
td {  
 border-right: 1px solid #C1DAD7;  
 border-bottom: 1px solid #C1DAD7;  
 background: #fff;  
 font-size:16px;
 padding: 6px 6px 6px 12px;  
 color: #4f6b72;  
}  
  
td.alt {  
 background: #F5FAFA;  
 color: #797268;  
}  
th.spec {  
 border-left: 1px solid #C1DAD7;  
 border-top: 0;  
 background: #fff url(images/bullet1.gif) no-repeat;  
 font: bold 15px Arial;
}  
th.specalt {  
 border-left: 1px solid #C1DAD7;  
 border-top: 0;  
 background: #f5fafa url(images/bullet2.gif) no-repeat;  
 font: bold 15px Arial;
 color: #797268;  
}  
/*---------for IE 5.x bug*/  
html>body td{ font-size:16px;}