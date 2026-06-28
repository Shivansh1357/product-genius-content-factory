"""
personas.py

The 10 companies in the Product Genius ICP, each enriched with the research
signals the factory uses to personalize. These are not mail-merge fields. Each
"pain", "hook", and "trigger" is a real, specific observation about the account
that the writer is instructed to weave in, never to restate as a bullet.

Segment + platform together drive two things automatically:
  - tone   (founder | operator | exec)
  - offer  (self-serve trial | sales-assisted A/B | enterprise A/B on a slice)
"""

from dataclasses import dataclass, field


@dataclass
class Account:
    id: str
    name: str
    category: str
    revenue: str
    platform: str
    shopify: bool
    segment: str            # "PLG", "Mid-market", "Enterprise"
    tone: str               # "founder" | "operator" | "exec"
    persona_name: str
    persona_title: str
    first_name: str         # "there" when we do not have a named individual
    lift_category: str
    pain: str
    hook: str
    trigger: str
    signals: list = field(default_factory=list)


ACCOUNTS = {
    "thirdlove": Account(
        id="thirdlove", name="ThirdLove", category="Apparel (intimates DTC)",
        revenue="$60m online", platform="Shopify", shopify=True,
        segment="Mid-market", tone="operator",
        persona_name="Heidi Zak", persona_title="CEO & Co-founder", first_name="Heidi",
        lift_category="Apparel",
        pain="fit and size discovery is the entire conversion problem in online "
             "intimates, and it still happens on a static page",
        hook="ThirdLove built a brand on a hard truth: most bras do not fit, and "
             "helping a woman find the one that does is the whole game.",
        trigger="public growth story on Shopify and a brand thesis built entirely on fit",
        signals=[
            ("Shopify since 2015", "Install is under an hour, not an engineering project"),
            ("Brand thesis = fit", "Discovery is the natural place to extend it"),
            ("Apparel category", "+34% revenue per session in our A/B tests"),
        ],
    ),
    "southern": Account(
        id="southern", name="Southern Baked Pie", category="Specialty Foods",
        revenue="$5m", platform="Shopify", shopify=True,
        segment="PLG", tone="founder",
        persona_name="Amanda Wilbanks", persona_title="Founder & CEO", first_name="Amanda",
        lift_category="Specialty Foods",
        pain="a seasonal gifting business lives or dies on a few big weeks, and a "
             "static homepage treats the first-time gift buyer the same as the regular",
        hook="I love what you have built: the bakeries, the Pie of the Month, the gift "
             "boxes. That gifting business lives on a few big weeks a year.",
        trigger="active gifting and subscription expansion plus founder media exposure",
        signals=[
            ("Shopify, founder-run", "You set it up yourself in under an hour"),
            ("Seasonal gifting spikes", "First-time gift buyers are who a learning feed converts"),
            ("Specialty food category", "+26% revenue per session in our A/B tests"),
        ],
    ),
    "abc": Account(
        id="abc", name="ABC Carpet & Home", category="Furnishings",
        revenue="$30m online", platform="Shopify", shopify=True,
        segment="Mid-market", tone="operator",
        persona_name="Head of DTC", persona_title="E-commerce lead (CEO Aaron Rose for the smaller call)",
        first_name="there", lift_category="Furnishings",
        pain="high-consideration, one-of-a-kind home goods live or die on "
             "inspiration-led discovery, not a search box",
        hook="ABC Carpet & Home is one of the most loved names in furnishings, and the "
             "online job is to make that in-store sense of discovery happen on a screen.",
        trigger="post-ownership refresh and active site and merchandising rework",
        signals=[
            ("On Shopify", "Install is under an hour, no replatform required"),
            ("Refresh underway", "A learning feed rides the redesign you are already doing"),
            ("Furnishings category", "+25% revenue per session in our A/B tests"),
        ],
    ),
    "thredup": Account(
        id="thredup", name="ThredUp", category="Apparel (resale)",
        revenue="$300m online", platform="Proprietary stack", shopify=False,
        segment="Enterprise", tone="exec",
        persona_name="James Reinhart", persona_title="CEO & Co-founder (or VP Product)",
        first_name="James", lift_category="Apparel",
        pain="every SKU in resale is one of a kind, so discovery is the core "
             "battleground, and you already build personalization in-house",
        hook="ThredUp has put real engineering into AI discovery, which is exactly why "
             "the next conversation is build-versus-buy, not whether discovery matters.",
        trigger="2025 rebrand and AI feature suite, heavy personalization investment",
        signals=[
            ("Builds personalization in-house", "We lead with the part that is hard to build"),
            ("One-of-a-kind inventory", "Cold-start on every SKU is what the LIM solves"),
            ("Apparel / resale", "+34% revenue-per-session benchmark in apparel"),
        ],
    ),
    "jtv": Account(
        id="jtv", name="JTV", category="Jewelry", revenue="$350m total",
        platform="Custom (React/Oracle)", shopify=False,
        segment="Enterprise", tone="exec",
        persona_name="Kevin Cleary", persona_title="CEO (turnaround) / VP E-commerce",
        first_name="Kevin", lift_category="Jewelry",
        pain="a video-commerce model built for cable is migrating to digital and "
             "marketplaces, where the on-site discovery experience has to do the selling",
        hook="JTV is moving a video-commerce model off cable and onto digital, and a "
             "scrolling, learning feed is the closest digital analog to what made the channel work.",
        trigger="new CEO and channel expansion onto Amazon and Macy's",
        signals=[
            ("Video-commerce DNA", "A TikTok-style feed is a natural translation"),
            ("New CEO, turnaround mode", "A measurable revenue lever fits the mandate"),
            ("Jewelry category", "+33% revenue per session in our A/B tests"),
        ],
    ),
    "yurman": Account(
        id="yurman", name="David Yurman", category="Jewelry (luxury)",
        revenue="$100m online", platform="Salesforce Commerce Cloud", shopify=False,
        segment="Enterprise", tone="exec",
        persona_name="VP E-commerce", persona_title="/ Chief Digital Officer",
        first_name="there", lift_category="Jewelry",
        pain="luxury jewelry conversion online hinges on storytelling and styling "
             "guidance, the how-to-stack-and-layer moment a product grid cannot deliver",
        hook="For David Yurman, the online job is to recreate the styling conversation "
             "that happens at the counter: how to stack, how to layer, what pairs with what.",
        trigger="high-cadence collection launches and celebrity campaigns",
        signals=[
            ("Salesforce Commerce Cloud", "We integrate via tag and API, no replatform"),
            ("Styling-led purchase", "A feed carries the layering story per shopper"),
            ("Jewelry category", "+33% revenue per session in our A/B tests"),
        ],
    ),
    "kohls": Account(
        id="kohls", name="Kohl's", category="Apparel (department store)",
        revenue="$5,000m online", platform="Custom enterprise", shopify=False,
        segment="Enterprise", tone="exec",
        persona_name="Arianne Parisi", persona_title="Chief Digital Officer (started 2025)",
        first_name="Arianne", lift_category="Apparel",
        pain="declining comps and a stated mandate to fix on-site findability mean every "
             "point of digital conversion is under the microscope",
        hook="You stepped into a clear mandate: fix findability and lift digital conversion "
             "while comps are under pressure. That is a revenue-per-session problem, and it is measurable.",
        trigger="new CDO and CEO in 2025, turnaround and findability mandate",
        signals=[
            ("New CDO, fresh mandate", "A reversible A/B test fits a new regime"),
            ("Findability is the stated gap", "Discovery is precisely what the feed improves"),
            ("Apparel / department", "+34% revenue-per-session benchmark in apparel"),
        ],
    ),
    "tractor": Account(
        id="tractor", name="Tractor Supply", category="Specialty Retail",
        revenue="$1,800m online", platform="Custom (Azure)", shopify=False,
        segment="Enterprise", tone="exec",
        persona_name="Rick Lockton", persona_title="SVP E-commerce / Hal Lawton, CEO",
        first_name="there", lift_category="Specialty Retail",
        pain="most online orders are buy-online-pickup-in-store, so lifting basket size "
             "and online conversion in an omnichannel flow is the stated focus",
        hook="Tractor Supply is already public about leaning into AI for ecommerce. The "
             "question is which AI moves a number, and revenue per session is the cleanest one.",
        trigger="public AI investment and an OpenAI partnership, Final Mile expansion",
        signals=[
            ("Already buying AI tooling", "We come in on the metric that matters"),
            ("BOPIS-heavy, basket-size focus", "A feed lifts attach inside the session"),
            ("Specialty retail / hard goods", "Double-digit revenue-per-session lift"),
        ],
    ),
    "envy": Account(
        id="envy", name="enVy Pillow", category="Furnishings (bedding)",
        revenue="$1m", platform="Shopify", shopify=True,
        segment="PLG", tone="founder",
        persona_name="Kim & Kathy", persona_title="Co-founders (Registered Nurses)",
        first_name="there", lift_category="Furnishings",
        pain="a brand built on one hero pillow is expanding into a full catalog, and a "
             "static page cannot cross-sell or educate the way a guided feed can",
        hook="You built enVy around one hero product, and now you are expanding into a real "
             "catalog. That shift is exactly when a site needs to start cross-selling for you.",
        trigger="product-line expansion and a heavy influencer and affiliate motion",
        signals=[
            ("Shopify, founder-run", "You install it yourself in under an hour"),
            ("Hero product to full catalog", "A learning feed handles cross-sell"),
            ("Furnishings / bedding", "+25% revenue per session in our A/B tests"),
        ],
    ),
    "inspiranza": Account(
        id="inspiranza", name="Inspiranza Designs", category="Jewelry",
        revenue="$4m", platform="Shopify", shopify=True,
        segment="PLG", tone="founder",
        persona_name="Diane & Dawn", persona_title="Co-founders", first_name="there",
        lift_category="Jewelry",
        pain="a large affordable-jewelry catalog where discovery and repeat purchase drive "
             "the business, and you already invest heavily in retention tooling",
        hook="You already run a serious retention stack: daily deals, a subscription box, a "
             "loyalty program. The missing piece is a storefront that personalizes discovery on the way in.",
        trigger="heavy retention and subscription motion on Shopify",
        signals=[
            ("Shopify, founder-run", "Installs in under an hour alongside your apps"),
            ("Big catalog, retention-driven", "Discovery is the front-door lever"),
            ("Jewelry category", "+33% revenue per session in our A/B tests"),
        ],
    ),
}


def get(account_id: str) -> Account:
    if account_id not in ACCOUNTS:
        raise KeyError(
            f"Unknown account '{account_id}'. Known: {', '.join(ACCOUNTS)}"
        )
    return ACCOUNTS[account_id]
