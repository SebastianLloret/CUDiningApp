'use strict';

let express = require('express');
let app = express();
let bodyParser = require('body-parser');
let https = require('https');
let fs = require('fs');
let scraper = require('./scraper');

let pdfLinks = [];

scraper('https://housing.colorado.edu/dining/menus', (error, result) => {
  for (let i = 0; i < result.h4Tags.length; i++){
    let children = result.h4Tags[i.toString()].children;
    for (let j = 0; j < children.length; j++){
      if (children[j].attribs && children[j].attribs.href){
      pdfLinks.push(children[j].attribs.href);
      };
    };
  };

  for(let i = 0; i < pdfLinks.length; i++){
    let file = fs.createWriteStream("./PDFs/" + pdfLinks[i].split('/files')[1]);
    let request = https.get(pdfLinks[i], response => {
      response.pipe(file);
      console.log("Downloaded " + pdfLinks[i].split('/files')[1])
      if (i == 1 - pdfLinks.length){
        process.exit();
      };
    });
  };
});
