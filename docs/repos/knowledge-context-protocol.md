# knowledge-context-protocol

*A structured metadata standard that makes knowledge navigable by AI agents.*

| Field | Value |
| --- | --- |
| **GitHub** | [https://github.com/Cantara/knowledge-context-protocol](https://github.com/Cantara/knowledge-context-protocol) |
| **Language** | Java · TypeScript · Python |
| **Stars** | 3 |
| **Last updated** | 2026-03-08 |

---

## README

# Knowledge Context Protocol (KCP)

> A structured metadata standard that makes knowledge navigable by AI agents.

**KCP is to knowledge what MCP is to tools.**

→ [**Website**](https://cantara.github.io/knowledge-context-protocol/) · [**Read the spec**](https://github.com/Cantara/knowledge-context-protocol/blob/main/SPEC.md) · [Read the proposal](https://github.com/Cantara/knowledge-context-protocol/blob/main/PROPOSAL.md)

The [Model Context Protocol](https://modelcontextprotocol.io) defines how agents connect to tools.
KCP defines how knowledge is structured so those tools can serve it effectively.
MCP solved the tool connectivity problem. KCP addresses the knowledge structure problem that remains.

---

## The Problem with llms.txt

Jeremy Howard's [llms.txt](https://llmstxt.org) solved a real problem: it gives AI agents a
canonical, machine-readable index of a website. For personal sites and small documentation sets,
it works well.

But llms.txt has six structural limitations that matter at scale:

| Limitation | What it means |
|-----------|---------------|
| **Flat topology** | Lists what exists. Cannot express that A depends on B, or that C supersedes D. |
| **No selective loading** | All or nothing: the index (small) or the full dump (huge). No middle ground. |
| **No intent metadata** | A URL and a description. No way to say what task this knowledge is relevant to. |
| **No freshness signal** | Cannot distinguish a document written yesterday from one written three years ago. |
| **No tooling connection** | A static file. No query interface, no dependency graph, no retrieval integration. |
| **Scale collapse** | Works for 27 blog posts. Fails for 8,934 files across an enterprise. |

These are structural limitations, not incidental ones. A bigger text file does not solve them.

---

## What KCP Provides

KCP is a file format specification — a `knowledge.yaml` manifest you drop at the root of a
project or documentation site. It adds the metadata layer that llms.txt cannot express:

- **Topology**: what depends on what, what supersedes what
- **Intent**: what task or question each knowledge unit answers
- **Freshness**: when each unit was last validated, and against what
- **Selective loading**: agents query by task context, not by URL guessing
- **Audience targeting**: which units are for humans, which for agents, which for both
- **Access control**: `access`, `auth_scope`, `auth.methods` for multi-tenant agent systems
- **Delegation**: `delegation` block controls whether and how agents may re-delegate tasks
- **Compliance**: `compliance` block carries data residency, regulations, and sensitivity

---

## The Spec

### Root Manifest: `knowledge.yaml`

```yaml
kcp_version: "0.7"
project: <name>
version: 1.0.0
updated: <ISO date>
language: <BCP 47 tag>             # optional — default for all units
license: <SPDX identifier>        # optional — default for all units
indexing: open | read-only | no-train | none  # optional — default for all units
hints:                             # optional — manifest-level aggregate hints
  total_token_estimate: <integer>
  recommended_entry_point: <unit-id>
  has_summaries: true | false
trust:                             # optional — publisher provenance
  provenance:
    publisher: <string>
    publisher_url: <string>
    contact: <string>
  audit:                           # optional — traceability requirements (v0.6+)
    agent_must_log: true | false
    require_trace_context: true | false
auth:                              # optional — authentication methods (v0.5+)
  methods: [none, oauth2, api_key]
delegation:                        # optional — agent delegation policy (v0.7+)
  max_depth: <integer>             # 0 = no delegation; owner = depth 0
  require_capability_attenuation: true | false
  audit_chain: true | false
  human_in_the_loop: always | on-sensitive | never
compliance:                        # optional — data and regulatory constraints (v0.7+)
  data_residency: [<ISO 3166-1 alpha-2>, ...]
  sensitivity: public | internal | confidential | restricted
  regulations: [gdpr, hipaa, pci-dss, sox, nis2, eu-ai-act, ccpa, iso27001, nist-csf, fedramp, dora, apra]
  restrictions: [no-cross-border, no-cloud, no-third-party-ai, human-review-required, audit-required, encrypted-at-rest]
payment:                           # optional — default monetisation tier
  default_tier: free | metered | subscription

units:
  - id: <unique-identifier>
    path: <relative path to content file>
    kind: knowledge | schema | service | policy | executable  # optional; default: knowledge
    intent: "<What question does this answer?>"
    format: markdown | pdf | openapi | ...  # optional
    content_type: <MIME type>              # optional
    language: <BCP 47 tag>                 # optional
    scope: global | project | module
    audience: [human, agent, developer, operator, architect]
    license: <SPDX identifier or object>  # optional
    validated: <ISO date>
    update_frequency: hourly | daily | weekly | monthly | rarely | never  # optional
    indexing: open | read-only | no-train | none  # optional
    depends_on: [<unit-id>, ...]       # optional
    supersedes: <unit-id>              # optional
    triggers: [<keyword>, ...]         # optional
    hints:                             # optional — context window hints
      token_estimate: <integer>
      load_strategy: eager | lazy | never
      priority: critical | supplementary | reference
      density: dense | standard | verbose
      summary_available: true | false
      summary_unit: <unit-id>
      summary_of: <unit-id>
    access: public | authenticated | restricted  # optional; default: public
    auth_scope: <string>               # optional — scope/role required (v0.5+)
    sensitivity: public | internal | confidential | restricted  # optional
    deprecated: true | false          # optional; default: false
    delegation:                        # optional — per-unit override (v0.7+)
      max_depth: <integer>
      require_capability_attenuation: true | false
      audit_chain: true | false
      human_in_the_loop: always | on-sensitive | never
    compliance:                        # optional — per-unit override (v0.7+)
      data_residency: [<ISO 3166-1 alpha-2>, ...]
      sensitivity: public | internal | confidential | restricted
      regulations: [...]
      restrictions: [...]
    payment:                           # optional — override root default
      default_tier: free | metered | subscription

relationships:
  - from: <unit-id>
    to: <unit-id>
    type: enables | context | supersedes | contradicts
```

### Knowledge Unit Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Unique identifier within the project |
| `path` | yes | Relative path to the content file |
| `kind` | optional | Type of artifact: `knowledge` (default), `schema`, `service`, `policy`, `executable` |
| `intent` | yes | One sentence: what question does this unit answer? |
| `format` | optional | Content format: `markdown`, `pdf`, `openapi`, `json-schema`, `jupyter`, etc. |
| `content_type` | optional | Full MIME type for precise format identification |
| `language` | optional | BCP 47 language tag (e.g. `en`, `no`, `de`) |
| `scope` | yes | `global`, `project`, or `module` |
| `audience` | yes | Who this is for: `human`, `agent`, `developer`, `operator`, `architect` |
| `license` | optional | SPDX identifier or structured license object |
| `validated` | recommended | ISO date when content was last confirmed accurate |
| `update_frequency` | optional | How often content changes: `hourly`, `daily`, `weekly`, `monthly`, `rarely`, `never` |
| `indexing` | optional | AI crawling permissions: `open`, `read-only`, `no-train`, `none`, or structured object |
| `depends_on` | optional | Units that must be understood before this one |
| `supersedes` | optional | The unit-id this replaces |
| `triggers` | optional | Task contexts or keywords that make this unit relevant |
| `hints` | optional | Advisory context window hints: `token_estimate`, `load_strategy`, `priority`, `density`, `summary_available`, `summary_unit`, `summary_of` |
| `access` | optional | Who can fetch this unit: `public` (default), `authenticated`, `restricted` |
| `auth_scope` | optional | Opaque scope/role string required when `access: restricted` (v0.5+) |
| `sensitivity` | optional | Information classification: `public`, `internal`, `confidential`, `restricted` |
| `deprecated` | optional | If `true`, this unit is present but should not be used for new development |
| `delegation` | optional | Per-unit delegation policy override (v0.7+) |
| `compliance` | optional | Per-unit data residency and regulatory constraints (v0.7+) |
| `payment` | optional | Monetisation tier: `default_tier: free \| metered \| subscription` |

### Minimum Viable KCP

Five fields per unit are enough to start:

```yaml
kcp_version: "0.7"
project: my-project
version: 1.0.0
units:
  - id: overview
    path: README.md
    intent: "What is this project and how do I get started?"
    scope: global
    audience: [human, agent]
```

The standard allows complexity but does not demand it.

---

## Complete Example

```yaml
# knowledge.yaml
kcp_version: "0.7"
project: wiki.example.org
version: 1.0.0
updated: "2026-03-08"
language: en
license: "Apache-2.0"
indexing: open

trust:
  audit:
    agent_must_log: true
    require_trace_context: false

delegation:
  max_depth: 1
  require_capability_attenuation: true
  audit_chain: true
  human_in_the_loop: on-sensitive

units:
  - id: about
    path: about.md
    intent: "Who maintains this project? Background, current work, contact."
    scope: global
    audience: [human, agent]
    validated: "2026-03-08"
    update_frequency: monthly

  - id: methodology
    path: methodology/overview.md
    intent: "What development methodology is used? Principles, evidence, adoption."
    format: markdown
    scope: global
    audience: [developer, architect, agent]
    depends_on: [about]
    validated: "2026-03-08"
    triggers: ["methodology", "productivity", "workflow"]

  - id: compliance-policy
    path: policies/data-handling.md
    intent: "What data handling constraints apply to agents using this knowledge base?"
    scope: global
    audience: [agent, architect]
    validated: "2026-03-08"
    compliance:
      data_residency: [NO, EU]
      sensitivity: internal
      regulations: [gdpr, nis2]
      restrictions: [no-cross-border, audit-required]

relationships:
  - from: methodology
    to: compliance-policy
    type: context
  - from: about
    to: methodology
    type: context
```

---

## Adoption Gradient

KCP is designed to be adopted incrementally.

**Level 1 — Personal sites and small projects**
Drop a `knowledge.yaml` alongside your `llms.txt`. Add `id`, `path`, and `intent` for your key
pages. Five minutes. Immediately navigable by agents.

**Level 2 — Open source projects**
Add `depends_on`, `validated`, `auth_scope` (for any restricted units), and `hints` (at minimum
`token_estimate`, `load_strategy`, and the `summary_available` / `summary_unit` / `summary_of`
trio). Agents can now load documentation in dependency order, check freshness before acting on
it, and prefer short TL;DR files over full documents when answering common questions.

**Level 3 — Enterprise documentation**
Use the full field set including `triggers`, `audience`, `relationships`, and advanced hints
(`priority`, `density`, chunking). Add `auth.methods`, `trust.audit`, and `compliance` blocks.
Build knowledge-graph-navigable documentation that supports multiple agent roles querying the
same corpus with different task contexts and constrained context budgets.

**Level 4 — Agentic systems and multi-agent pipelines**
Add `delegation` constraints (root and per-unit), populate `compliance.regulations` and
`restrictions`, and set `trust.audit.agent_must_log`. KCP becomes a behavioural guardrail:
delegation depth, capability attenuation, and human-in-the-loop requirements are declared in the
manifest and enforced by KCP-aware agents and orchestrators.

---

## Relationship to HATEOAS

KCP shares a foundational insight with HATEOAS (Hypermedia As The Engine Of Application State):
typed, directional relationships between resources are necessary for navigation — a flat list is
not enough. KCP's `depends_on`, `supersedes`, and `relationships` fields are the same idea as
HATEOAS link relations.

The key difference is static vs dynamic. HATEOAS links are generated per-response based on live
resource state. KCP is a committed file: it declares topology at authoring time without a server.
Where KCP goes further: the `intent` field (what question does this unit answer?), `validated`
(human-confirmed freshness, not just file modification time), and `audience` targeting — concerns
that arise specifically when the consumer is a context-window-constrained AI agent rather than an
API client.

---

## Relationship to MCP and Synthesis

**MCP** (Model Context Protocol) defines how agents connect to tools. KCP defines how knowledge
is structured for those tools to serve.

**Synthesis** is a knowledge infrastructure tool and reference implementation of a KCP-native
knowledge server. It indexes workspaces — code, documentation, configuration, PDFs — and serves
them via MCP with sub-second retrieval. KCP is the format specification; Synthesis is one engine
that implements it.

`synthesis export --format kcp` will generate a `knowledge.yaml` from an existing
Synthesis index automatically.

---

## Relationship to A2A (Agent-to-Agent Protocol)

Google's **A2A protocol** defines how agents discover each other and exchange tasks using *agent
cards* (`/.well-known/agent.json`). KCP and A2A operate at different layers:

| Layer | Protocol | Handles |
|-------|----------|---------|
| Transport / invocation | A2A | Agent discovery, task lifecycle, message exchange |
| Knowledge access | KCP | What knowledge an agent may read, under what constraints |

A2A agent cards say *what an agent can do*. A KCP manifest says *what an agent may know*.
An agent card can embed or reference a `knowledge.yaml` to declare the knowledge scope of its
skills. The `delegation` and `compliance` blocks added in KCP v0.7 are designed to interoperate
with A2A's capability model.

The [KCP simulation suite](https://github.com/Cantara/knowledge-context-protocol/tree/main/examples)
includes 4 scenarios (150 adversarial tests) validating this integration:

- **a2a-agent-card** — A2A card embedding a KCP manifest
- **scenario1-energy-metering** — IoT data pipeline with residency constraints
- **scenario2-legal-delegation** — Multi-jurisdiction legal workflow with max_depth enforcement
- **scenario3-financial-aml** — AML compliance with audit chain and human-in-the-loop

---

## Ecosystem

| Package | Language | Description |
|---------|----------|-------------|
| [`kcp-mcp`](https://www.npmjs.com/package/kcp-mcp) v0.11.0 | TypeScript | MCP bridge — expose any `knowledge.yaml` as MCP resources, tools, and prompts |
| [`kcp-mcp`](https://github.com/Cantara/knowledge-context-protocol/tree/main/bridge/java) v0.11.0 | Java | Full-parity Java MCP bridge |
| [`kcp-mcp`](https://pypi.org/project/kcp-mcp/) v0.6.0 | Python | Python MCP bridge |
| [`kcp-commands`](https://www.npmjs.com/package/kcp-commands) v0.11.0 | TypeScript | 284 YAML manifests for common CLI tools — syntax injection + noise filtering for AI agents |
| [`kcp-memory`](https://github.com/Cantara/kcp-memory) | YAML | KCP manifests for AI session memory patterns |

---

## Status

**Current:** v0.7 (stable spec — March 2026)

- **[SPEC.md](https://github.com/Cantara/knowledge-context-protocol/blob/main/SPEC.md)** — Normative specification (field definitions, validation rules, conformance levels)
- **[PROPOSAL.md](https://github.com/Cantara/knowledge-context-protocol/blob/main/PROPOSAL.md)** — The case for a knowledge architecture standard
- **[RFC-0001](https://github.com/Cantara/knowledge-context-protocol/blob/main/RFC-0001-KCP-Extended.md)** — Extended capabilities overview (F/H/I/J/K/L/N promoted to v0.3–v0.4 core)
- **[RFC-0002](https://github.com/Cantara/knowledge-context-protocol/blob/main/RFC-0002-Auth-and-Delegation.md)** — Auth and delegation (`access`, `auth`, `auth_scope` promoted to v0.5; `delegation` promoted to v0.7)
- **[RFC-0003](https://github.com/Cantara/knowledge-context-protocol/blob/main/RFC-0003-Federation.md)** — Cross-manifest federation (`manifests` block, `external_depends_on`, hub-and-spoke)
- **[RFC-0004](https://github.com/Cantara/knowledge-context-protocol/blob/main/RFC-0004-Trust-and-Compliance.md)** — Trust, provenance, and compliance (`trust`, `compliance` promoted to v0.7; `trust.audit` promoted to v0.6)
- **[RFC-0005](https://github.com/Cantara/knowledge-context-protocol/blob/main/RFC-0005-Payment-and-Rate-Limits.md)** — Payment and rate-limit metadata (`payment`, `rate_limits` blocks)
- **[RFC-0006](https://github.com/Cantara/knowledge-context-protocol/blob/main/RFC-0006-Context-Window-Hints.md)** — Context window hints (promoted to SPEC.md §4.10 in v0.4)
- **parsers/** — Reference implementations (Python, Java, TypeScript) — all at v0.7
- **bridge/** — MCP servers: expose any `knowledge.yaml` as MCP resources, tools, and prompts (TypeScript · Python · Java)
- **examples/** — A2A integration simulator + 4 adversarial scenarios (150 tests)

---

## Contributing

Open an issue to:
- Propose additions to the field set
- Share a use case that the current spec does not cover
- Report a gap or ambiguity in the format

The goal is a standard that solves the real problem without demanding complexity from those who
do not need it.

---

## License

Apache V2.

*Proposed by [eXOReaction AS](https://www.exoreaction.com) — builders of Synthesis, based in Oslo, Norway.*
