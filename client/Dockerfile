# Step 1: Build the Angular app
FROM node:18 AS build

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Build the Angular app
RUN npm run build --prod

EXPOSE 4200

CMD ["npm", "run", "start"]
