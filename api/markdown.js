const fs = require('fs');
const path = require('path');

module.exports = (req, res) => {
  try {
    const filePath = path.join(process.cwd(), 'index.md');
    const content = fs.readFileSync(filePath, 'utf8');
    res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
    res.setHeader('x-markdown-tokens', '1450');
    res.setHeader('Vary', 'Accept');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.status(200).send(content);
  } catch (err) {
    res.status(500).send('Error reading markdown: ' + err.message);
  }
};
