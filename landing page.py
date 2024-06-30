def create_landing_page(title, heading, subheading, background_image_url):
    # HTML content for the landing page
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-image: url('{background_image_url}');
                background-size: cover;
                background-position: center;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                color: white;
            }}
            .content {{
                background-color: rgba(0, 0, 0, 0.6);
                padding: 20px;
                border-radius: 10px;
                max-width: 80%;
            }}
            h1 {{
                font-size: 3rem;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.5rem;
                margin-top: 0;
            }}
        </style>
    </head>
    <body>
        <div class="content">
            <h1>{heading}</h1>
            <p>{subheading}</p>
        </div>
    </body>
    </html>
    """
    return html_content

# Example usage:
title = "Welcome to Our Site"
heading = "Discover Something Amazing"
subheading = "Explore our services and products!"
background_image_url = "https://example.com/background.jpg"

# Generate the HTML content for the landing page
landing_page_html = create_landing_page(title, heading, subheading, background_image_url)

# Write the HTML content to a file (optional)
with open('landing_page.html', 'w') as file:
    file.write(landing_page_html)

print("Landing page created successfully!")
