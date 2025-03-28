const fs = require('fs');
const axios = require('axios');

const username = 'scorpio21'; // Reemplaza con tu nombre de usuario

async function fetchRepos() {
  const response = await axios.get(`https://api.github.com/users/${username}/repos`);
  return response.data;
}

function generateRepoMarkdown(repos) {
  return repos
    .map(repo => `- [${repo.name}](${repo.html_url}): ${repo.description}`)
    .join('\n');
}

async function updateReadme() {
  const repos = await fetchRepos();
  const repoMarkdown = generateRepoMarkdown(repos);

  const readmeContent = `# 🌟 Bienvenido a Mi GitHub

¡Hola! Soy [${username}](https://github.com/${username}), un apasionado desarrollador. Aquí puedes encontrar información sobre mis proyectos.

## 🚀 Proyectos Destacados

${repoMarkdown}

## 📫 Contacto

- **Correo**: [tu-email@example.com](mailto:tu-email@example.com)
- **LinkedIn**: [tu-linkedin](https://www.linkedin.com/in/tu-linkedin)

¡Gracias por visitar mi perfil!
`;

  fs.writeFileSync('README.md', readmeContent);
}

updateReadme().catch(error => console.error(error));