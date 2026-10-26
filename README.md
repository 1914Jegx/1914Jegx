# Jhonatan González

**AI-first product engineer** · Medellín, Colombia (UTC−5) · open to remote work · **[Portfolio → cimadium.com/jegx/en](https://cimadium.com/jegx/en/)**

I have built software since 2024, and today I build and run it in production with Claude Code as my main tool. I define the product, decide the architecture, direct the implementation, review and test what ships, and operate it once it's live. The AI writes most of the code; the decisions and the responsibility are mine.

- **Measure, then decide.** I chose the model for a customer-service agent by benchmarking 10 models on the real codebase. The winner scored higher on quality and cost US$0.002 per reply in the benchmark, against US$0.024 for the previous model in production (8× cheaper like-for-like). [Read the case study →](https://github.com/1914Jegx/llm-agent-cost-benchmark)
- **Tests and CI are the gate.** About 9,600 automated test cases across Recover, Vital and O.D.A.; at Recover alone, 890 pull requests merged through CI.
- **I run what I ship.** Real payments through signed, idempotent webhooks, infrastructure as code, and cost and latency measured in production.

## In production

| Project | What it is | Impact |
|---|---|---|
| [**Recover**](https://recoversds.com) | E-commerce for a security-systems company. Next.js 16, React 19, TypeScript, Postgres + Drizzle, on Hetzner + Cloudflare with OpenTofu | 15,410-product catalog · quoting engine with 222 quotes in Aug–Sep 2026 · Bold payments via HMAC-signed webhooks · 890 merged PRs · ~6,200 test cases |
| [**NIA**](https://recoversds.com) (Recover) | AI sales agent that answers Recover's customers | Benchmarked 10 models on the real codebase: better quality and US$0.002 per reply in the benchmark vs US$0.024 for the previous model in production ([case study](https://github.com/1914Jegx/llm-agent-cost-benchmark)) |
| [**Vital**](https://esvital.group) | Booking platform for mental-health professionals, with mandatory Wompi payment. Freelance, Mar–Oct 2026 | First paid appointment in Sep 2026 · 268 PRs · ~2,100 test cases |
| [**O.D.A.**](https://dagotrading.com) | Telegram SaaS bot with paid subscriptions: card (Wompi) and crypto (NowPayments). Python, aiogram, FastAPI, Postgres | Idempotent payment webhooks · multi-model AI routing · 1,284 pytest tests |
| [**PRISMA**](https://prisma.cimadium.com) | Turns one video into an edited episode, clips, subtitles, thumbnails and a scheduled YouTube upload (ffmpeg, Whisper, LLM) | Multi-tenant on Cloudflare Workers + D1 + R2 · a 134 MB episode processed in ~2 min |
| [**Carnudos**](https://carnudos.com) | Online ordering for a restaurant | Every order prints automatically as an ESC/POS ticket at the point of sale |
| **NEMO** (personal) | Local-first personal assistant | Hybrid search in SQLite (vectors + FTS5 + RRF): semantic search 1,378 ms → 20 ms at 92.7% recall@10 |

**Stack:** TypeScript · Next.js · React · Python · FastAPI · aiogram · PostgreSQL + Drizzle · SQLite · Cloudflare Workers, D1, R2 · Hetzner · OpenTofu · Bold, Wompi, NowPayments · ffmpeg, Whisper · Claude Code

**Contact:** [cimadium.com/jegx/en](https://cimadium.com/jegx/en/) · [linkedin.com/in/1914jegx](https://linkedin.com/in/1914jegx) · [1914jegx@gmail.com](mailto:1914jegx@gmail.com)

---

<sub>En español: construyo software desde 2024 y lo opero en producción usando IA (Claude Code) como herramienta principal. Portafolio: [cimadium.com/jegx](https://cimadium.com/jegx/). Busco trabajo remoto; escríbeme a 1914jegx@gmail.com.</sub>
