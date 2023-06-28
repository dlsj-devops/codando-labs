const puppeteer = require('puppeteer');

console.log('Bem vindo ao bot conversor');

{async () => {
    const browser = awai puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://example.com');
    await page.screemshot({path: 'example.png'})
    
    awair.browser.close();
    
}}