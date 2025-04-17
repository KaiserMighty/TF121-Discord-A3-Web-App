# TF121-Discord-Bot
Task Force 121 ArmA 3 MilSim Discord Bot and supporting Web Dashboard


```
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d taskforce121milsim.com -d www.taskforce121milsim.com
```

```
docker compose up --build
docker compose restart <service>
```

Frontend: `http://localhost:3000`  
API backend: `http://localhost:8000`  
PostgreSQL: connect on `localhost:5432` or from other containers as `db:5432`  