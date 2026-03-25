# LinkedIn Post Templates

Reference templates for creating LinkedIn content from arsenal findings.
Use these by telling Claude: "Create a LinkedIn post about TIP-{NNN}" or
"Create a LinkedIn post referencing this video: {URL}".

---

## PROMPT 6 — Post from Arsenal Finding

Use when: you want to share a tip, tool, or configuration from the arsenal.

### Input to provide
- Entry: TIP-{NNN} or topic/tool name
- Context (pre-filled): IT Manager who builds with Claude Code, audience is IT professionals and developers

### Output: 3 Variants

**Variant A — Discovery angle**
Frame: "I found this tool that solves X, here's why it's worth your attention."
Practical, not hype. Focus on the problem it solves, not the technology itself.

**Variant B — How I use it**
Frame: "Here's how I integrated X into my workflow and what changed."
Personal experience. Concrete before/after. What you expected vs. what happened.

**Variant C — Bigger picture**
Frame: "This tool represents a trend. Here's what it means for our industry."
Thought leadership without fluff. Tie the specific tool to a broader shift.

### Structure for each variant
1. **Hook** (first 2 lines before "see more") — must earn the click without being clickbait
2. **Body** — 150-250 words, short paragraphs (2-3 sentences max), no walls of text
3. **Call to action** — genuine question or invitation ("What's your approach to X?"), never "like and share"
4. **Hashtags** — 3-5 relevant, no generic (#AI, #Tech alone)
5. **GitHub link** — include naturally if the entry has one ("The repo: {url}")

### Tone rules
- Knowledgeable but approachable
- Write like a senior IT professional sharing a discovery with peers
- Show you've actually used it (or evaluated it seriously)
- Avoid: "game-changer", "you won't believe", "revolutionary", "excited to share"
- Emojis: sparingly — →, ✅, 🔧 are acceptable. No emoji spam.
- No bullet-point walls. Use prose with occasional lists.

---

## PROMPT 7 — Post Referencing a Video

Use when: you found a useful video and want to amplify it while adding your professional layer.

### Input to provide
- Video URL
- What it shows (your description of the key points — you must describe it, Claude cannot watch)
- Creator name/handle

### Output: single LinkedIn post

The post must:
1. **Credit the creator prominently** — tag them in the post (@handle), include the URL
2. **Add YOUR professional perspective** — what the video doesn't cover, how you'd apply it in an IT/enterprise context, caveats, deeper analysis
3. **Position you as a curator** — not someone who just reshares, but someone who adds context
4. **Include a genuine "go watch this" CTA** — make people want to click the original video

### Why this structure works
Your audience follows you for your judgment, not for discovery alone.
The creator gets traffic. You get credibility as someone who contextualizes.
Both win.

### Same tone rules as PROMPT 6
No buzzwords. Short paragraphs. Real professional take, not a press release.

---

## Quick Reference — What NOT to Write

| Avoid | Use instead |
|-------|-------------|
| "I'm excited to share..." | Start with the problem or observation |
| "This is a game-changer" | State the specific benefit |
| "In today's fast-paced world..." | Skip the preamble, open with the hook |
| Bullet lists for everything | Mix prose and lists |
| 10 hashtags | 3-5 targeted ones |
| "Like and subscribe" | Ask a genuine question |

---

After writing, verify:
```bash
grep "PROMPT 6\|PROMPT 7\|Variant A\|Variant B\|Variant C" /c/Users/mbern/claude-arsenal/prompts/linkedin-templates.md | wc -l
```

Expected: 5 matches.
