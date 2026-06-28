"""
adapt.py

The Adapt + Channelize logic for offline mode. These functions compose the
source atoms with one account's profile into channel-ready drafts.

Important: every writer reads from the `atoms` dict it is handed, not from a
global. That is what makes the source a real input. Pass the cached whitepaper
atoms and you get one set of drafts; pass atoms extracted from a different
source (see extract.py and run.py --source) and the output changes.

Every string here is written without em-dashes; qa.py is the backstop.
"""

from .sources import ATOMS


def _cap(s: str) -> str:
    return s[0].upper() + s[1:] if s else s


def _install_line(a) -> str:
    if a.shopify and a.segment == "PLG":
        return ("it installs on your Shopify store in under an hour and there is "
                "nothing to train")
    if a.shopify:
        return ("it installs on Shopify in well under an hour, so it rides any "
                "redesign you are already running")
    return ("our team adds a JavaScript tag in about thirty minutes, no replatform, "
            "and you run it as a controlled A/B test on a slice of traffic")


def _offer_line(a) -> str:
    if a.segment == "PLG":
        return ("There is a 15-day trial, and the honest way to judge it is to let "
                "half your visitors see the feed and half see your current site, "
                "with revenue per session as the scoreboard.")
    if a.segment == "Mid-market":
        return ("The lowest-risk way to settle it is the same A/B test we ran: half "
                "your traffic on the feed, half on the site you have today, revenue "
                "per session as the scoreboard, on a 15-day trial.")
    return ("We do not ask you to believe the number. We ask you to run the same "
            "randomized A/B test we ran, on a slice of your traffic, with revenue "
            "per session as the metric.")


def write_blog(a, lift, atoms):
    cat = a.lift_category.lower()
    title = (
        "Your busiest weeks decide your year. Your website should get smarter in "
        "them, not slower."
        if a.lift_category == "Specialty Foods"
        else "The most expensive page on your store is the one nobody optimizes"
        if a.shopify
        else "The next point of conversion is not on your product page. It is before it."
    )
    paras = [
        f"Most {a.category.split(' (')[0].lower()} teams pour their attention into the "
        f"product page and the checkout. The page almost nobody optimizes is the one in "
        f"between: the moment a shopper lands, scans, and silently decides whether anything "
        f"here is for them. For {a.name}, {a.pain}.",

        f"We have a number for how expensive that moment is. In controlled A/B tests, "
        f"adapting to each shopper in real time delivered this: {atoms['headline_stat']}. "
        f"In {cat} specifically, the lift averaged {lift} percent. That is the same traffic "
        f"and the same catalog, converting more of the people already on the page.",

        f"The usual fix is a recommendation engine trained on historical data. It works "
        f"eventually, for shoppers who look like last quarter's shoppers. It struggles with "
        f"the cases that matter most: the first-time visitor, the new collection, the shopper "
        f"outside the fat part of the curve. {atoms['betsey_story']} The lesson was simple. "
        f"If you wait for statistical significance before you act, you are always optimizing "
        f"for a shopper who has already left. {_cap(atoms['speed_line'])}.",

        f"Instead of pulling levers after the data confirms a trend, the system works "
        f"differently. {_cap(atoms['mechanism'])}. In practice {atoms['few_interactions']}, "
        f"and it keeps adapting as interests and inventory move. {_cap(atoms['no_data'])}.",

        f"Picture the homepage reading the room for {a.name}: a shopper lands, the feed opens "
        f"on what they came for, then reorders itself with every swipe, surfacing the next "
        f"best product and the answer to the question they have not typed yet. {_cap(a.pain)} "
        f"is, not coincidentally, exactly the kind of problem that gets cheaper when the page "
        f"learns in real time instead of in quarters. The product page and the checkout are "
        f"mostly solved. The expensive, unoptimized middle is where the next {lift} percent is sitting.",
    ]
    return {"type": "blog", "title": title, "paragraphs": paras}


def write_linkedin(a, lift, atoms):
    posts = []
    posts.append({
        "voice": "Ben Vigoda, Founder & Chief Scientist",
        "text": (
            "Here is the thing we learned building this, and it took me a while to accept it.\n\n"
            f"{atoms['betsey_story']}\n\n"
            f"{_cap(atoms['speed_line'])}. That is the whole idea, and most teams have not "
            "caught up to it yet. We stopped optimizing for the shopper who already left and "
            "started optimizing for the one still scrolling."
        ),
    })
    if a.segment == "Enterprise":
        p2 = (
            "\"We would just build this ourselves.\"\n\n"
            f"Fair instinct, and for a team like {a.name}'s, a real option. So here is the "
            "honest version.\n\n"
            f"The hard part is not a recommendation widget. {_cap(atoms['mechanism'])}, working "
            "on the first-time visitor and the brand-new SKU. "
            f"{_cap(atoms['darpa'])}, and it is what we maintain so your team does not have to.\n\n"
            "Build-versus-buy here is not \"can we.\" It is \"is this the thing we want our best "
            "engineers spending two years on.\" For most teams, the answer is no."
        )
    else:
        p2 = (
            "\"We are too small for AI personalization.\"\n\n"
            "I hear this from good operators every week, and it is backwards.\n\n"
            "The old recommendation playbook needed a mountain of historical data, so it "
            f"rewarded the giants and punished everyone else. {_cap(atoms['no_data'])}. "
            f"{_cap(atoms['few_interactions'])}.\n\n"
            f"So the question is not \"do I have enough traffic.\" It is \"how much revenue am I "
            f"leaving on the sessions I already have.\" For {a.lift_category.lower()} brands in "
            f"our tests, the answer averaged {lift} percent."
        )
    posts.append({"voice": "Noah Maffitt, Chief Growth Officer", "text": p2})
    posts.append({
        "voice": "Ben Vigoda, Founder & Chief Scientist",
        "text": (
            f"{_cap(a.pain)}.\n\n"
            "A grid of pretty photos does not solve that. Neither does a search box, because it "
            "asks the shopper to already know what they want.\n\n"
            f"{_cap(atoms['mechanism'])}, surfacing the next best thing and the one detail that "
            "resolves the doubt they have not voiced. It learns them in the session, not over a "
            "quarter.\n\n"
            f"For {a.name}, discovery is the moat. Most teams just have not pointed their best "
            "technology at it yet."
        ),
    })
    return {"type": "linkedin", "posts": posts}


def write_email(a, lift, atoms):
    g = "Hi there," if a.first_name == "there" else f"Hi {a.first_name},"
    sign = "Noah Maffitt\nChief Growth Officer, Product Genius"
    emails = [
        {"day": "Day 0", "subject": "the page between your ad and your checkout",
         "body": (
            f"{g}\n\n{a.hook}\n\n"
            "We built an AI that turns the few seconds after a shopper lands into a feed that "
            "adapts as they scroll, surfacing the next best product instead of making them dig. "
            f"In controlled A/B tests, the headline result was this: {atoms['headline_stat']}. "
            f"In {a.lift_category.lower()} specifically, the lift averaged {lift} percent.\n\n"
            f"It learns from the live session, so {_install_line(a)}.\n\n"
            f"Worth fifteen minutes to show you what it would look like on a {a.name} page?\n\n{sign}"
         )},
        {"day": "Day 3", "subject": "the proof behind the number, without cherry-picking",
         "body": (
            f"{g}\n\n"
            "Quick follow-up with the proof, since the number deserves a footnote.\n\n"
            "We ran randomized A/B tests: half of traffic saw the normal site, half saw the same "
            f"site with our feed added. We measured revenue per session, and {atoms['conservative']}. "
            f"{a.lift_category} brands averaged {lift} percent.\n\n"
            "The mechanism behind it is a model that adapts to each shopper in the moment rather "
            "than waiting for a trend to become significant. On a fast-moving brand, that was the "
            "entire difference between a lift that held and one that evaporated by lunch.\n\n"
            f"I can send the whitepaper with the learning curves, or walk you through it live. "
            f"Which is easier?\n\n{sign}"
         )},
        {"day": "Day 7",
         "subject": ("the build-versus-buy question, answered honestly"
                     if a.segment == "Enterprise"
                     else "\"too small for AI\"? actually the opposite"),
         "body": (
            (f"{g}\n\n"
             "A team as capable as yours has surely asked whether you would just build this. "
             "Fair question, so here is the straight answer.\n\n"
             "The hard part is not the widget. It is a learning system that adapts faster than "
             "statistics can confirm a change, works without third-party data, and performs on "
             f"the first-time visitor and the new SKU. {_cap(atoms['darpa'])}, and it is what we "
             "maintain so your team can stay on the roadmap they care about.\n\n"
             "On your side it is a tag and an API call, run as a controlled A/B test, not a "
             "platform project. If the instinct is still to build, I am glad to be a sounding "
             f"board on what that actually takes. No pitch.\n\n{sign}")
            if a.segment == "Enterprise"
            else
            (f"{g}\n\n"
             "One myth I want to bust, because a lot of founders believe it.\n\n"
             "The old personalization tools needed a ton of data, so they only helped the big "
             f"players. The one we build is different. {_cap(atoms['few_interactions'])}, and "
             f"{atoms['no_data']}.\n\nFor {a.name} that is the point. {_cap(a.pain)}. A site that "
             "reads each visitor and answers their real question in the moment converts a lot "
             f"more of them. Happy to show you what it would look like on your product pages.\n\n{sign}")
         )},
        {"day": "Day 12", "subject": "a test, not a leap of faith",
         "body": (
            f"{g}\n\n"
            "Last note from me, and it is the lowest-risk way to settle this.\n\n"
            f"{_offer_line(a)} {_cap(_install_line(a))}. If the lift is not there, you have lost "
            "almost nothing.\n\n"
            "If now is not the moment, no problem, and I will stop landing in your inbox. If you "
            f"want to see it on a real {a.name} page first, reply with a time and I will bring "
            "the mockup.\n\n"
            "Either way, I think the discovery problem is the most interesting one in your "
            f"category, and it is the natural place to extend what you have already built.\n\n{sign}"
         )},
    ]
    return {"type": "email", "emails": emails}


_WRITERS = {"blog": write_blog, "linkedin": write_linkedin, "email": write_email}


def write(channel, account, lift, atoms=None):
    return _WRITERS[channel](account, lift, atoms or ATOMS)
