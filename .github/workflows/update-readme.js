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

  const readmeContent = `# 👋 Hola, soy Scorpio21

¡Bienvenido a mi perfil de GitHub! Soy un apasionado desarrollador con interés en diversas tecnologías y proyectos.

## 🚀 Proyectos Destacados

${repoMarkdown}

## 📊 Estadísticas de GitHub

![Estadísticas de GitHub](https://github-readme-stats.vercel.app/api?username=${username}&show_icons=true&theme=dark)

## 🌱 Actualmente estoy aprendiendo

- [Tecnología 1](#)
- [Tecnología 2](#)

## 📫 Cómo contactarme

- **Correo**: [tu-email@example.com](mailto:tu-email@example.com)
- **LinkedIn**: [tu-linkedin](https://www.linkedin.com/in/tu-linkedin)

---

¡Gracias por visitar mi perfil!
`;

  fs.writeFileSync('README.md', readmeContent);
}

updateReadme().catch(error => console.error(error));