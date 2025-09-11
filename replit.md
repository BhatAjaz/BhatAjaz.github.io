# Overview

This is a Jekyll-based static website for Dr. Ajaz Ahmad Bhat's research laboratory at Universiti Brunei Darussalam. The site serves as an academic portfolio showcasing the lab's research activities, publications, team members, and projects in artificial intelligence, cognitive robotics, and related fields. It features a responsive design with sections for home, team profiles, publications, research projects, news, and contact information including job vacancies.

**Architecture Status (September 2025)**: The entire codebase has been comprehensively refactored to eliminate ALL hardcoded values, creating a fully configuration-driven, maintainable system with zero hardcoding and complete customization flexibility through centralized configuration files and design tokens.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Configuration-Driven Architecture

**Complete Hardcoding Elimination**: The site now operates with ZERO hardcoded values. Everything is controlled through:

- **`_data/site_config.yml`**: Master configuration file controlling all behavioral settings, limits, timing, paths, and functionality
- **Design Token System**: Comprehensive SASS variables in `_sass/0-base/_variables.sass` for all colors, typography, spacing, and visual properties
- **Data-Driven Components**: All templates and JavaScript consume configuration dynamically without fallback values

### Site Configuration System (`_data/site_config.yml`)

The centralized configuration file controls:

**Content Limits & Display**
- Publication/project/news display limits for all sections
- Slider rotation intervals and interaction timing
- Search functionality parameters and filtering options
- Content truncation lengths and excerpt sizes

**Asset Management**
- Image directory paths for all content types (news, publications, team, projects)
- Fallback image paths and file extensions
- Image dimension specifications for responsive design
- Supported file formats and asset optimization settings

**Interactive Behavior**
- Slider autoplay timing and transition effects  
- Search debounce timing and filtering sensitivity
- Hover effect parameters and animation durations
- Mobile breakpoints and responsive behavior

**Example Configuration Structure:**
```yaml
content:
  limits:
    slider_items: 6
    recent_publications: 4
    featured_projects: 3
  timing:
    slider_interval: 4000
    search_debounce: 300
images:
  directories:
    news_directory: "/assets/images/news/"
    publications_directory: "/assets/images/publications/"
  fallback_image: "/assets/images/publications/research-general.jpeg"
```

## Design Token System

**Comprehensive SASS Variables** (`_sass/0-base/_variables.sass`):

**Color System**
- `$primary`, `$secondary`, `$background`, `$text`, `$link` - Complete color palette
- All components use token-based colors with zero hardcoded hex/rgb values
- Consistent theming across all interface elements

**Typography Tokens**
- `$font-primary`, `$font-secondary` - Font family hierarchy
- Fluid typography with responsive scaling using clamp() functions
- Consistent text sizing and line height throughout

**Spacing & Layout**
- `$element-spacing`, `$section-padding` - Consistent spacing system
- `$radius-sm`, `$radius-md`, `$radius-lg` - Border radius tokens
- `$shadow-sm`, `$shadow-md`, `$shadow-lg` - Box shadow system

**Responsive Design Tokens**
- Breakpoint variables for consistent mobile-first design
- Flexible grid systems with configurable column counts
- Adaptive spacing and sizing for all screen sizes

## Frontend Architecture

The site uses Jekyll as the static site generator with a component-based architecture utilizing Liquid templating. The design follows a modular approach with reusable includes for navigation, headers, search functionality, and footer components. JavaScript functionality is implemented using jQuery for navigation toggles, smooth scrolling, and interactive features like project sliders with automatic rotation.

**Enhanced User Interaction**: All card containers across the website now feature clickable functionality with hover cursor effects. When users hover over publication cards, team member cards, project cards, or news items, they display a pointer cursor and the entire card becomes clickable, navigating to the corresponding detail page. This provides intuitive navigation beyond just the "Read More" links.

**Content Type Indicators**: The main page slider features clear content type badges with colored text boxes displaying "PUBLICATION" (blue) or "NEWS" (orange) instead of ambiguous icons, making it immediately obvious to users what type of content they're viewing.

**Dynamic Component System**: All templates are now fully configuration-driven:
- **`content-mixer.html`**: Dynamically combines content based on site_config.yml limits and settings
- **`slider-component.html`**: Reads rotation timing and display limits from configuration without hardcoded fallbacks
- **`site-scripts.html`**: All JavaScript behavior controlled by data attributes from Jekyll configuration
- **Modular Includes**: Complex content generation logic extracted into reusable, configurable components

## CSS Architecture (Token-Based)

The SASS codebase uses a comprehensive design token system with zero hardcoded values:

**Design Token Integration**
- All colors, dimensions, shadows, and typography use centralized variables
- `_sass/1-helpers/mixins.sass` contains reusable patterns using design tokens
- Eliminated redundant hardcoded rgb/hex colors and pixel values throughout

**Mixin System**
- **Shared Mixins**: Reusable patterns for container headers, page layouts, hover effects using design tokens
- **Consolidated Page Styles**: Unified layouts using shared `@include page-layout` mixin with token-based styling
- **Standardized Components**: All interface elements use consistent token-based styling patterns

**Token-Based Styling Examples**
- Search inputs: `background-color: $background`, `box-shadow: $shadow-sm`
- Content boxes: `border: 1px solid rgba($primary, 0.1)`, `border-radius: $radius-md`
- Interactive elements: Hover effects using `rgba($primary, 0.3)` for consistent transparency

## Template System

Jekyll layouts and includes are organized hierarchically with a default layout containing the base HTML structure. All components are now configuration-driven:

**Dynamic Templating**
- Reusable components consume site_config.yml for limits, paths, and behavior
- Navigation with mobile hamburger menu using configurable breakpoints
- Search inputs with live filtering using configurable timing and sensitivity
- Tag-based color coding with design token integration

**Configuration Integration**
- All templates use `{{ site.data.site_config }}` for dynamic values
- Image paths, display limits, and timing all controlled by configuration
- No hardcoded fallback values - everything references central configuration

## Content Management

Content is managed through YAML data files that store information for projects, publications, team members, news items, and job vacancies. All content rendering is now configuration-driven through site_config.yml settings.

**Dynamic Image Management**
- **`_data/news_images.yml`**: Configurable image mappings with extension settings
- Fallback images controlled through site_config.yml (no hardcoded paths)
- Responsive image handling with configurable dimensions

**Project Navigation System**: Projects use a streamlined navigation system where each project YAML file contains a `proj_id` field that directly corresponds to the project page URL (e.g., `proj_id: "knowledge-graph-completion"` creates `/project/knowledge-graph-completion/`). This eliminates redundancy from the previous dual-field system and provides clean, semantic URLs that match the project identifiers.

**Projects Page Layout**: The projects page displays as a responsive card-based layout. Projects appear as attractive cards in a 3-column grid (responsive to 2-column on tablets, 1-column on mobile) with centered images, clean typography, and hover effects using design tokens. Card display limits are controlled by site_config.yml.

**Publications Structure**: Publications are organized with SEO-friendly URLs using individual YAML files within the `_data/publications/` folder. Each publication uses descriptive file names based on titles with corresponding HTML pages in the `/publication/` directory. The system supports all 26 research publications with clean, readable URLs. Display limits and truncation settings are controlled through site_config.yml.

**Team Structure**: The team is organized into structured academic position categories:
- Principal Investigator
- Research Scientists & PostDocs  
- PostGraduate Students
- Bachelors Students
- Alumni (Collaborators)
- Other Collaborators

Each team member has their own dedicated HTML file in the `/team/` directory using a `member_id` field for clean URLs (e.g., `/team/Alice-Newton/`). Team card styling uses design tokens for consistent visual presentation.

**News/Blog System**: News operates as a full Jekyll blog system with individual posts in `_posts/` directory. Rich content support includes markdown formatting and embedded media. All styling uses design token system for consistent presentation.

## Responsive Design

The architecture implements mobile-first responsive design with CSS media queries and flexible layouts using design tokens. Navigation adapts to mobile with a collapsible menu system, and content sections use CSS Grid and Flexbox for responsive layouts. All breakpoints and spacing use configurable design tokens rather than hardcoded values.

## Search and Filtering

Client-side search functionality is fully configuration-driven:
- Search timing and debounce settings controlled by site_config.yml
- Filter limits and display counts configurable per content type
- Tag-based categorization with design token color coding
- Real-time filtering parameters controlled through central configuration

# Configuration Management Guide

## Making Site-Wide Changes

**Visual Customization**: Edit `_sass/0-base/_variables.sass` to change:
- Colors: `$primary`, `$secondary`, `$background`, `$text`, `$link`
- Typography: `$font-primary`, `$font-secondary`
- Spacing: `$element-spacing`, `$section-padding`
- Effects: `$radius-*`, `$shadow-*` tokens

**Behavioral Customization**: Edit `_data/site_config.yml` to change:
- Content display limits for any section
- Slider timing and interaction parameters
- Search functionality and filtering settings
- Asset paths and fallback configurations

**Asset Management**: Update `_data/news_images.yml` for:
- Image mappings and associations
- File extensions and format preferences
- Fallback image configurations

## Maintenance Benefits

**Zero Hardcoding**: Complete elimination means:
- Single-point changes affect entire site consistently
- No hunting through multiple files to change colors or limits
- Configuration drift impossible - all settings centralized
- Easy theme swapping through design token updates

**Scalability**: The token-based system supports:
- Easy addition of new content types with consistent styling
- Rapid prototyping with configurable behavior
- A/B testing through configuration switches
- Multi-theme support through token file swapping

# External Dependencies

## Static Site Generation
- **Jekyll**: Ruby-based static site generator for building and deploying the website
- **Liquid Templating**: Template engine for dynamic content rendering with configuration integration

## Frontend Libraries
- **jQuery 3.7.1**: JavaScript library for DOM manipulation, event handling, and AJAX functionality (timing controlled by site_config.yml)
- **Google Fonts**: External font loading for typography system (fonts controlled by design tokens)

## Social Media Integration
- **Google Scholar**: Academic profile linking for research publications and citations
- **Gmail**: Email contact integration for laboratory correspondence
- **YouTube**: Video content integration for research demonstrations and presentations

## Asset Management

The site uses local asset management with fully configurable paths:
- CSS stylesheets generated from SASS with design token system
- JavaScript files with configuration-driven behavior
- Image resources organized through configurable directory structure
- All paths and extensions controlled through site_config.yml and data files

**Performance**: External dependencies minimized with essential libraries loaded from CDNs. All internal assets use configuration-driven optimization and responsive handling.