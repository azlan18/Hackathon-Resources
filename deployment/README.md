# Deployment & Infrastructure

## Free VPS Credits

### Vultr
- **URL**: https://www.vultr.com/promo/try250
- **Free Credits**: $250-300 for 30 days (new users)
- **Features**:
  - High-performance SSD cloud servers
  - Global data centers
  - 1-click apps (Docker, WordPress, etc.)
  - DDoS protection & 100% SLA uptime

**How to Claim:**
1. Sign up with new email (not existing accounts)
2. Use promo code: `FLY300VULTR` or `250VULTRFLY`
3. Credits auto-apply (or manually in Billing → Promo Code)
4. Deploy immediately without upfront charges
5. Credits valid for 30 days

**Deployment Example:**
```bash
# After setting up Vultr instance

# 1. SSH into server
ssh root@your-server-ip

# 2. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# 3. Deploy your app
git clone https://github.com/your-username/your-project
cd your-project
docker-compose up -d

# 4. Configure firewall
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
```

## Quick Deployment Options

### From Faculty PDF:
- **Frontend/Fullstack**: Vercel, Netlify
- **Backend**: Render, Railway
- **Database**: Supabase, Neon, MongoDB Atlas
- **Emergency**: Ngrok for localhost tunneling

### Comparison Table

| Platform | Best For | Free Tier | Deploy Time |
|----------|----------|-----------|-------------|
| Vercel | Next.js/React | Unlimited | ~2 mins |
| Netlify | Static sites | 100 GB bandwidth | ~2 mins |
| Render | Docker/Python/Node | 750 hrs/month | ~5 mins |
| Railway | Any backend | $5 credit | ~3 mins |
| Vultr | ML models, heavy compute | $250-300 credits | ~10 mins |

## Best Practices
1. **Deploy early**: 2 hours before deadline, not 20 minutes
2. **Record backup video**: Use Loom if live demo fails
3. **Use Ngrok as last resort**: Tunnels localhost to public URL
4. **Test on mobile**: Judges often test on phones
5. **Custom domain**: Use GitHub Student Pack for free .tech domain

## Environment Variables
```bash
# .env file structure
DATABASE_URL=postgresql://user:pass@host:5432/db
OPENAI_API_KEY=sk-...
TWILIO_ACCOUNT_SID=AC...
TWILIO_AUTH_TOKEN=...
```

**Never commit .env files!**
```bash
# .gitignore
.env
.env.local
.env.*.local
```
