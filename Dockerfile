# Use the official NGINX base image
FROM nginx:latest
# Copy the HTML file to the NGINX directory
COPY index.html /usr/share/nginx/html/
# Expose port 80
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]