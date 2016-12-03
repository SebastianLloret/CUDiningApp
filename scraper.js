'use strict';

let cheerio = require('cheerio');
let request = require('request');

module.exports = (link, callback) => {

  request(link, (error, response, body) => {
    if (error) {
      return callback({'error': error}, null);
    }

    let $ = cheerio.load(body);
    let pdfLinks = $('h4');
    return callback(null, {pdfLinks});
  });
};
