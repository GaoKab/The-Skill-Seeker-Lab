"""
NodeRail Terms of Service — Structural Outline (v2)

Strategic/legal reference document. Not executable code.
Defines the key provisions that must appear in NodeRail's Terms
of Service, organized by section with rationale and draft language.

This is an outline for legal counsel, not a final legal document.
Every section should be reviewed by an attorney before publication.
"""


# ===================================================================
# PLAIN-LANGUAGE SUMMARY (must appear at top of published ToS)
# ===================================================================

PLAIN_LANGUAGE_SUMMARY = {
    "title": "What this means for you",
    "purpose": (
        "This summary appears at the top of the published Terms of Service "
        "so users understand their rights without reading legal text."
    ),
    "points": [
        {
            "heading": "You own your work",
            "plain": (
                "Everything you create on NodeRail belongs to you. "
                "We only have permission to display and serve it "
                "through the platform."
            ),
        },
        {
            "heading": "DOIs are permanent",
            "plain": (
                "Once your work receives a DOI, it stays published "
                "forever — even if you delete your account. That's "
                "how DOIs work. You agree to this when you accept a DOI."
            ),
        },
        {
            "heading": "Reviews are opinions",
            "plain": (
                "Expert reviews are professional opinions, not guarantees. "
                "If a reviewer validates something that later turns out "
                "to be wrong, that's not their fault or ours."
            ),
        },
        {
            "heading": "AI access respects you",
            "plain": (
                "If AI systems access your work through our API, they "
                "must credit you. They can reference your work with "
                "attribution. They cannot train on it without a separate "
                "agreement. You can opt out of AI access entirely."
            ),
        },
        {
            "heading": "You can leave anytime",
            "plain": (
                "You can export all your data and delete your account "
                "whenever you want. DOI-linked work stays published "
                "(see above), but everything else is removed."
            ),
        },
        {
            "heading": "We don't sell your data",
            "plain": (
                "We don't sell, rent, or trade your personal data or "
                "content to anyone. Ever."
            ),
        },
        {
            "heading": "Your work survives even if we don't",
            "plain": (
                "If NodeRail ever shuts down, all DOI-linked work gets "
                "deposited with Zenodo (backed by CERN) so your DOIs "
                "keep resolving. We give at least 6 months notice."
            ),
        },
    ],
}


# ===================================================================
# CORE PROMISE
# ===================================================================

CORE_PROMISE = (
    "You own your work. NodeRail ensures it survives, remains "
    "attributable, and is used responsibly."
)

# ===================================================================
# 1. CONTENT OWNERSHIP
# ===================================================================

CONTENT_OWNERSHIP = {
    "principle": (
        "Authors own their work. NodeRail receives a license, not "
        "ownership. This is non-negotiable and central to trust."
    ),

    "provisions": [
        {
            "title": "Author retains all intellectual property rights",
            "detail": (
                "All content uploaded, created, or published on NodeRail "
                "— including nodes, descriptions, frameworks, measurements, "
                "field notes, and any associated metadata — remains the "
                "intellectual property of the author or their institution "
                "as applicable. NodeRail does not claim ownership of any "
                "user-generated content."
            ),
        },
        {
            "title": "License grant to NodeRail",
            "detail": (
                "By publishing content on NodeRail, the author grants "
                "NodeRail a non-exclusive, worldwide, royalty-free license "
                "to display, distribute, cache, index, and make available "
                "the content through the NodeRail platform, API, and "
                "associated services. This license is necessary for "
                "NodeRail to operate — displaying content to other users, "
                "serving it through the API, and including it in graph "
                "visualizations and search results."
            ),
        },
        {
            "title": "License survives account deletion for DOI content",
            "detail": (
                "For content that has received a DOI, the license grant "
                "is irrevocable for the purpose of maintaining the DOI "
                "resolution and the archived version of the work. This "
                "is required by DOI permanence standards. See section 7 "
                "(DOI Permanence) for details."
            ),
        },
        {
            "title": "License terminates for non-DOI content upon deletion",
            "detail": (
                "For content that has not received a DOI, the license "
                "terminates when the author deletes the content or their "
                "account. NodeRail will remove such content from active "
                "display within 30 days of deletion request, subject to "
                "backup retention policies."
            ),
        },
        {
            "title": "Institutional content ownership",
            "detail": (
                "When content is created under an institutional account, "
                "the ownership terms are governed by the institutional "
                "data agreement (see section 5). The default is that the "
                "individual author retains ownership unless the "
                "institution's agreement specifies otherwise."
            ),
        },
    ],
}


# ===================================================================
# 2. REVIEWER LIABILITY
# ===================================================================

REVIEWER_LIABILITY = {
    "principle": (
        "Reviews are expert opinions, not certifications of truth. "
        "Reviewers cannot be held liable for incorrect validation or "
        "for failing to identify errors in reviewed work."
    ),

    "provisions": [
        {
            "title": "Reviews are opinions, not warranties",
            "detail": (
                "Expert reviews on NodeRail represent the professional "
                "opinion of the reviewer at the time of review. A verdict "
                "of 'validated' or 'novel' does not constitute a warranty, "
                "guarantee, or certification that the reviewed work is "
                "correct, complete, or free from error. Reviews are one "
                "input in an ongoing process of intellectual development."
            ),
        },
        {
            "title": "No liability for review outcomes",
            "detail": (
                "Reviewers shall not be held liable for any damages, "
                "losses, or consequences arising from their review "
                "verdicts, including but not limited to: incorrect "
                "validation of flawed work, failure to identify errors, "
                "or mischaracterization of novelty. Users who rely on "
                "reviewed content do so at their own professional "
                "judgment."
            ),
        },
        {
            "title": "Review permanence and immutability",
            "detail": (
                "Completed reviews are part of the intellectual lineage "
                "of a structure and cannot be deleted by the reviewer "
                "after completion. A reviewer may append a correction or "
                "updated opinion, but the original review remains in the "
                "record. This preserves the integrity of the lineage."
            ),
        },
        {
            "title": "Reviewer identity and accountability",
            "detail": (
                "Reviews are attributed to the reviewer by name and "
                "institutional affiliation. Anonymous review is not "
                "supported. This transparency is a design choice: "
                "attributed reviews carry more weight and create "
                "accountability without creating legal liability."
            ),
        },
        {
            "title": "NodeRail is not liable for reviewed content",
            "detail": (
                "NodeRail provides the platform for expert review but "
                "does not endorse, verify, or guarantee any content, "
                "reviewed or otherwise. The presence of a review or a "
                "DOI does not imply NodeRail's endorsement of the "
                "content's accuracy or validity."
            ),
        },
    ],
}


# ===================================================================
# 3. AI API USAGE TERMS
# ===================================================================

AI_API_USAGE = {
    "principle": (
        "NodeRail's API makes structured, reviewed knowledge available "
        "to AI systems. Usage terms must protect authors while enabling "
        "legitimate machine access to validated knowledge."
    ),

    "provisions": [
        {
            "title": "API access requires authentication and agreement",
            "detail": (
                "Access to NodeRail content via the API requires a "
                "registered API key and explicit agreement to these "
                "terms. Unauthenticated scraping of NodeRail content "
                "is prohibited."
            ),
        },
        {
            "title": "Attribution is mandatory",
            "detail": (
                "AI systems that access NodeRail content via the API "
                "must attribute the source. Attribution must include: "
                "the structure's title, author(s), DOI (if issued), and "
                "the URL 'noderail.web.app'. The specific format of "
                "attribution may vary by use case but must be present "
                "in any output derived from NodeRail content."
            ),
        },
        {
            "title": "Training vs. retrieval distinction",
            "detail": (
                "NodeRail content accessed via the API may be used for "
                "retrieval-augmented generation (RAG) and real-time "
                "reference with attribution. Use of NodeRail content "
                "for training machine learning models (including LLMs) "
                "requires a separate training data license agreement "
                "with NodeRail and, where applicable, consent from the "
                "content authors. Bulk download for training purposes "
                "without a training data license is prohibited."
            ),
        },
        {
            "title": "No misrepresentation of source",
            "detail": (
                "AI systems must not present NodeRail content as their "
                "own original output. When an AI system surfaces "
                "content derived from NodeRail, it must be identifiable "
                "as sourced material, not generated knowledge."
            ),
        },
        {
            "title": "Rate limits and fair use",
            "detail": (
                "API access is subject to rate limits based on the "
                "API tier. Excessive or abusive access patterns — "
                "including systematic bulk retrieval designed to "
                "replicate the NodeRail database — are prohibited and "
                "may result in API key revocation."
            ),
        },
        {
            "title": "Author opt-out for AI access",
            "detail": (
                "Authors may opt out of having their content served "
                "through the AI API. Opted-out content will be excluded "
                "from API responses but will remain accessible through "
                "the web interface. Opt-out is per-structure and can be "
                "changed at any time."
            ),
        },
        {
            "title": "Revenue sharing for API-accessed content",
            "detail": (
                "NodeRail reserves the right to implement a revenue "
                "sharing model where authors whose content is accessed "
                "via the paid AI API receive a share of API revenue "
                "proportional to access volume. Terms of any such "
                "program will be communicated separately."
            ),
        },
    ],
}


# ===================================================================
# 4. DATA STORAGE AND PRIVACY
# ===================================================================

DATA_STORAGE_PRIVACY = {
    "principle": (
        "NodeRail stores user data on Google Cloud Platform (Firebase / "
        "Firestore). Privacy practices must comply with GDPR and "
        "applicable regulations."
    ),

    "provisions": [
        {
            "title": "What data NodeRail collects",
            "detail": (
                "Account data: name, email, institutional affiliation, "
                "ORCID (optional). Usage data: login timestamps, "
                "structures created/edited, reviews completed. Content "
                "data: all nodes, edges, versions, and reviews created "
                "by the user. NodeRail does not collect payment "
                "information directly — payments are processed by a "
                "third-party provider."
            ),
        },
        {
            "title": "Where data is stored",
            "detail": (
                "All data is stored on Google Cloud Platform (Firebase / "
                "Cloud Firestore), with servers in the United States. "
                "Backups are maintained in geographically separate "
                "regions for disaster recovery. DOI metadata is "
                "additionally stored with Zenodo (CERN, Switzerland)."
            ),
        },
        {
            "title": "Data encryption",
            "detail": (
                "Data is encrypted in transit (TLS 1.2+) and at rest "
                "(AES-256) using Google Cloud's default encryption. "
                "Firebase Authentication handles credential storage "
                "with industry-standard security practices."
            ),
        },
        {
            "title": "No sale of personal data",
            "detail": (
                "NodeRail does not sell, rent, or trade personal data "
                "or user content to third parties. Aggregate, "
                "anonymized usage statistics may be shared publicly "
                "(e.g., 'X structures published this month') but never "
                "individual data."
            ),
        },
        {
            "title": "GDPR compliance",
            "detail": (
                "Users in the European Economic Area have the right to "
                "access, correct, and delete their personal data. "
                "Requests can be made via email. NodeRail will respond "
                "within 30 days. Note that DOI-linked content is "
                "subject to the DOI permanence provisions in section 7."
            ),
        },
        {
            "title": "Cookies and analytics",
            "detail": (
                "NodeRail uses essential cookies for authentication "
                "and session management. Analytics (if implemented) "
                "will use privacy-respecting, cookieless analytics or "
                "will require explicit consent."
            ),
        },
    ],
}


# ===================================================================
# 5. INSTITUTIONAL DATA AGREEMENTS
# ===================================================================

INSTITUTIONAL_DATA_AGREEMENTS = {
    "principle": (
        "Institutions need clear terms about who owns what, where "
        "data lives, and what happens when the agreement ends. These "
        "provisions override individual terms where applicable."
    ),

    "provisions": [
        {
            "title": "Institutional vs. individual content ownership",
            "detail": (
                "Institutional data agreements specify whether content "
                "created by institutional members belongs to the "
                "individual author, the institution, or is jointly "
                "owned. The default (absent a specific agreement) is "
                "individual ownership with the institution having a "
                "non-exclusive license to use the work internally."
            ),
        },
        {
            "title": "Data residency requirements",
            "detail": (
                "For institutions with data residency requirements, "
                "NodeRail will provide documentation of data storage "
                "locations. Custom data residency (e.g., EU-only "
                "storage) may be available under Enterprise tier "
                "agreements at additional cost."
            ),
        },
        {
            "title": "Institutional admin controls",
            "detail": (
                "Institutional admins can manage members, set "
                "visibility defaults for institutional content, and "
                "receive aggregate usage reports. Admins cannot read "
                "or modify individual members' drafts (exploratory "
                "status content) without the member's permission."
            ),
        },
        {
            "title": "Data export upon agreement termination",
            "detail": (
                "If an institutional agreement is terminated, the "
                "institution receives a full export of all institutional "
                "content in JSON format within 60 days. DOI-linked "
                "content remains accessible on NodeRail per DOI "
                "permanence requirements, but is no longer editable "
                "by institutional members."
            ),
        },
        {
            "title": "Compliance and audit",
            "detail": (
                "NodeRail will cooperate with reasonable audit requests "
                "from institutional customers regarding data handling "
                "practices. Security questionnaires and compliance "
                "documentation (SOC 2, etc.) will be provided as "
                "available."
            ),
        },
        {
            "title": "Single sign-on and identity",
            "detail": (
                "Institutional agreements may include SSO integration "
                "(SAML 2.0 / OAuth) so that institutional members "
                "authenticate through their existing identity provider. "
                "Available under Enterprise tier."
            ),
        },
    ],
}


# ===================================================================
# 6. ACCOUNT TERMINATION AND DATA PORTABILITY
# ===================================================================

ACCOUNT_TERMINATION = {
    "principle": (
        "Users can leave NodeRail at any time and take their data. "
        "But DOIs are permanent — that's the whole point."
    ),

    "provisions": [
        {
            "title": "Voluntary account deletion",
            "detail": (
                "Users may request account deletion at any time. "
                "Account deletion removes the user's profile, login "
                "credentials, and personal data. Content handling "
                "depends on DOI status (see below)."
            ),
        },
        {
            "title": "Data export before deletion",
            "detail": (
                "Before account deletion, users can export all their "
                "content (nodes, edges, versions, reviews) in JSON "
                "format. NodeRail will provide export functionality "
                "in the platform UI. Users are encouraged to export "
                "before requesting deletion."
            ),
        },
        {
            "title": "Non-DOI content upon deletion",
            "detail": (
                "Content that has not received a DOI will be removed "
                "from public display within 30 days of account "
                "deletion. Edges connecting to other users' content "
                "will be severed. The deleted user's structures will "
                "no longer appear in the graph. Backup copies may "
                "persist for up to 90 days for disaster recovery "
                "purposes and will then be permanently deleted."
            ),
        },
        {
            "title": "DOI content upon deletion",
            "detail": (
                "Content that has received a DOI will remain accessible "
                "in read-only, archived form. The DOI will continue to "
                "resolve. The author attribution will remain. The "
                "content cannot be edited or evolved further. This is "
                "a fundamental requirement of the DOI system: once a "
                "DOI is issued, the identified resource must remain "
                "available. Authors agree to this when they accept a "
                "DOI for their work."
            ),
        },
        {
            "title": "Termination by NodeRail",
            "detail": (
                "NodeRail reserves the right to terminate accounts "
                "that violate these terms, including but not limited "
                "to: publishing fraudulent or plagiarized content, "
                "abusing the review system, or violating API usage "
                "terms. Terminated users will receive 30 days notice "
                "and an opportunity to export their data, except in "
                "cases of egregious violation."
            ),
        },
        {
            "title": "Data portability format",
            "detail": (
                "Exported data will be in a documented JSON format "
                "consistent with the NodeRail data model. The export "
                "includes: all nodes with full metadata, all edges, "
                "all version history, all reviews (authored by and "
                "received by the user), and DOI records. The format "
                "is designed to be human-readable and importable into "
                "other systems."
            ),
        },
    ],
}


# ===================================================================
# 7. DOI PERMANENCE
# ===================================================================

DOI_PERMANENCE = {
    "principle": (
        "DOIs are permanent. This is a core promise of the DOI system "
        "and of NodeRail. A DOI issued by NodeRail will resolve to "
        "the identified work for as long as the DOI system exists."
    ),

    "provisions": [
        {
            "title": "DOIs survive account deletion",
            "detail": (
                "If an author deletes their account, any DOI-linked "
                "content remains accessible in archived, read-only "
                "form. The DOI continues to resolve. This is not "
                "optional — it is a requirement of DOI registration "
                "and a commitment NodeRail makes to the scholarly "
                "community."
            ),
        },
        {
            "title": "DOIs survive platform changes",
            "detail": (
                "NodeRail commits to maintaining DOI resolution even "
                "if the platform undergoes significant changes, "
                "including domain changes, architecture changes, or "
                "ownership changes. DOI metadata registered with "
                "Zenodo/DataCite provides an additional layer of "
                "permanence independent of NodeRail's operational "
                "status."
            ),
        },
        {
            "title": "DOI content cannot be deleted by the author",
            "detail": (
                "Once a DOI is issued, the author cannot delete the "
                "content. The author may request that an erratum or "
                "retraction notice be attached, but the original "
                "content and DOI remain. This mirrors the practice "
                "in traditional academic publishing."
            ),
        },
        {
            "title": "DOI content can be versioned",
            "detail": (
                "Authors can publish new versions of DOI-linked "
                "content. Each major version may receive its own DOI. "
                "The original DOI continues to resolve to the original "
                "version. A 'latest version' DOI may also be provided "
                "that resolves to the most recent version."
            ),
        },
        {
            "title": "Platform shutdown provisions",
            "detail": (
                "In the event that NodeRail ceases operations, all "
                "DOI-linked content will be deposited with Zenodo or "
                "an equivalent long-term repository, and DOI "
                "resolution will be transferred to that repository. "
                "NodeRail will provide at least 6 months notice of "
                "any planned shutdown. This commitment is part of "
                "NodeRail's responsibility as a DOI-issuing platform."
            ),
        },
        {
            "title": "Reviews are part of the DOI record",
            "detail": (
                "Expert reviews attached to DOI-linked content are "
                "considered part of the permanent record. Reviews "
                "cannot be deleted after DOI issuance. Reviewer "
                "attribution remains. This ensures the quality signal "
                "that makes NodeRail DOIs valuable is preserved."
            ),
        },
    ],
}


# ===================================================================
# TERMS STRUCTURE SUMMARY
# ===================================================================

TERMS_SECTIONS = [
    {"number": 1, "title": "Content Ownership", "key": "CONTENT_OWNERSHIP"},
    {"number": 2, "title": "Reviewer Liability", "key": "REVIEWER_LIABILITY"},
    {"number": 3, "title": "AI API Usage Terms", "key": "AI_API_USAGE"},
    {"number": 4, "title": "Data Storage and Privacy", "key": "DATA_STORAGE_PRIVACY"},
    {"number": 5, "title": "Institutional Data Agreements", "key": "INSTITUTIONAL_DATA_AGREEMENTS"},
    {"number": 6, "title": "Account Termination and Data Portability", "key": "ACCOUNT_TERMINATION"},
    {"number": 7, "title": "DOI Permanence", "key": "DOI_PERMANENCE"},
]

ADDITIONAL_SECTIONS_TODO = [
    "Acceptable Use Policy (what content is prohibited)",
    "Dispute Resolution (arbitration vs. courts, jurisdiction)",
    "Limitation of Liability (standard cap on damages)",
    "Indemnification (user indemnifies NodeRail for their content)",
    "Modification of Terms (how changes are communicated)",
    "Governing Law (jurisdiction)",
    "Severability (if one provision is invalid, the rest stand)",
    "Entire Agreement (this is the whole deal)",
]
