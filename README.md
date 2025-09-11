# Dr. Ajaz Ahmad Bhat's Research Laboratory Website

A modern, responsive Jekyll website showcasing research activities, publications, team members, and projects in artificial intelligence, cognitive robotics, and related fields at Universiti Brunei Darussalam.

## Features

- **🎨 Modern Design**: Clean, responsive layout that works on all devices
- **📚 Publication Management**: SEO-optimized URLs and easy content management
- **👥 Team Profiles**: Individual pages for lab members with social links
- **🔬 Project Showcase**: Detailed project descriptions with visual elements
- **📰 News & Updates**: Jekyll blog system for announcements and achievements
- **🔍 Search & Filter**: Real-time content filtering by tags and categories
- **🏷️ Smart Tagging**: Automatic color-coded tag system

## Quick Start

### Prerequisites
- Ruby 2.7 or higher
- Jekyll gem
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Install dependencies**:
   ```bash
   bundle install
   ```

3. **Run locally**:
   ```bash
   bundle exec jekyll serve --host 0.0.0.0 --port 5000 --livereload
   ```

4. **Open in browser**: Navigate to `http://localhost:5000`

## Project Structure

```
├── _data/              # Content data files (YAML)
├── _includes/          # Reusable components
├── _layouts/           # Page templates
├── _posts/             # Blog posts/news
├── _sass/              # Stylesheets
├── assets/             # Images, CSS, JavaScript
├── publication/        # Individual publication pages
├── project/            # Individual project pages
├── team/               # Team member pages
└── *.html              # Main site pages
```

## Content Management

All content is managed through YAML files in the `_data/` directory:

- **Team**: `_data/team.yml`
- **Publications**: `_data/publications/[publication-name].yml`
- **Projects**: Individual files in `_data/projects/` and `_data/projects_overview.yml`
- **News**: Individual files in `_posts/`

## Adding New Content

### New Team Member
1. Add entry to `_data/team.yml`
2. Create page: `team/Member-Name.html`
3. Add photo: `assets/img/team/`

### New Publication
1. Create: `_data/publications/publication-title.yml`
2. Create page: `publication/publication-title.html`
3. Add image: `assets/img/publications/`

### New Blog Post
Create: `_posts/YYYY-MM-DD-title.md`

## Customization

### Styling
- Edit SASS files in `_sass/`
- Color variables in `_sass/0-base/`
- Layout styles in `_sass/2-layouts/`

### Components
- Modify includes in `_includes/`
- Update layouts in `_layouts/`

## Deployment

### GitHub Pages
1. Push to main branch
2. Enable GitHub Pages in repository settings
3. Site builds automatically

### Manual Deployment
```bash
bundle exec jekyll build
# Upload _site/ folder to web server
```

## Documentation

For detailed instructions on content management, customization, and maintenance, see [DOCUMENTATION.md](DOCUMENTATION.md).

## Technical Details

- **Framework**: Jekyll 4.x
- **CSS**: SASS with modular architecture
- **JavaScript**: jQuery 3.7.1
- **Responsive**: Mobile-first design
- **SEO**: Optimized URLs and meta tags

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## License

This project is for academic use. Please contact Dr. Ajaz Ahmad Bhat for usage permissions.

## Contact

**Dr. Ajaz Ahmad Bhat**  
Principal Investigator  
Universiti Brunei Darussalam  
Email: [ajaz.bhat@ubd.edu.bn](mailto:ajaz.bhat@ubd.edu.bn)

---

*Built with ❤️ using Jekyll*