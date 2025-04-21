# Task Force 121 Web Application
Task Force 121 ArmA 3 MilSim Discord/A3 interface and supporting Web Dashboard

### SSL Certification
```
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d taskforce121milsim.com -d www.taskforce121milsim.com
```

### Common Docker Commands
```
docker compose up --build
docker compose restart <service>
docker compose down
```

### Development Environment
[docker-compose.override.yml](https://pastebin.com/raw/n4NbM0Vh)  
Frontend: `http://localhost:3000`  
API backend: `http://localhost:8000`  
PostgreSQL: connect on `localhost:5432` or from other containers as `db:5432`  

### Environment File
```
# .env

DISCORD_TOKEN=
DISCORD_CLIENT_ID=
DISCORD_CLIENT_SECRET=
DISCORD_REDIRECT_URI=http://localhost:5000/callback

DATABASE_URL=postgresql://postgres:password@db:5432/botdb
```
