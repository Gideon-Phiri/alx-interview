#!/usr/bin/node

// Importing the request module
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Base URL for the Star Wars API films endpoint
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the Star Wars API to get the film details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  
  // Parse the response body into JSON
  const filmData = JSON.parse(body);

  // Check if characters field exists
  if (!filmData.characters) {
    console.error('No characters found for this movie');
    return;
  }

  // Function to fetch character name
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  };

  // Iterate through character URLs, fetch, and print character names
  const characters = filmData.characters;
  const promises = characters.map(url => fetchCharacterName(url));

  // Resolve all promises and print each character name
  Promise.all(promises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(err => console.error('Error fetching character names:', err));
});
