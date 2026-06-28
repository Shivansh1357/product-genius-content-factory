# Forge output: JTV
_Target: Kevin Cleary, CEO (turnaround) / VP E-commerce. Segment: Enterprise. Platform: Custom (React/Oracle). Engine: offline-deterministic. Source: cached whitepaper atoms. Category lift used: 33%._

## Blog post

### The next point of conversion is not on your product page. It is before it.

Most jewelry teams pour their attention into the product page and the checkout. The page almost nobody optimizes is the one in between: the moment a shopper lands, scans, and silently decides whether anything here is for them. For JTV, a video-commerce model built for cable is migrating to digital and marketplaces, where the on-site discovery experience has to do the selling.

We have a number for how expensive that moment is. In controlled A/B tests, adapting to each shopper in real time delivered this: a 36 percent average lift in revenue per session across 25 brands and millions of sessions. In jewelry specifically, the lift averaged 33 percent. That is the same traffic and the same catalog, converting more of the people already on the page.

The usual fix is a recommendation engine trained on historical data. It works eventually, for shoppers who look like last quarter's shoppers. It struggles with the cases that matter most: the first-time visitor, the new collection, the shopper outside the fat part of the curve. On a fast-moving fashion brand the lift would hold for a week and then vanish within hours, on its own, because shopper interest, competitor pricing, and new drops had moved faster than our statistics could confirm. The fix was to act before the data was conclusive. The lesson was simple. If you wait for statistical significance before you act, you are always optimizing for a shopper who has already left. You have to move faster than the speed of statistics.

Instead of pulling levers after the data confirms a trend, the system works differently. An AI feed that adapts to each shopper as they scroll, learning from the live session instead of waiting for a trend to become statistically significant. In practice it picks up a useful signal in under a dozen interactions per shopper, and it keeps adapting as interests and inventory move. It learns from the live visit, so it needs no third-party data and no long training period, and it works on stores doing as few as ten thousand sessions a month.

Picture the homepage reading the room for JTV: a shopper lands, the feed opens on what they came for, then reorders itself with every swipe, surfacing the next best product and the answer to the question they have not typed yet. A video-commerce model built for cable is migrating to digital and marketplaces, where the on-site discovery experience has to do the selling is, not coincidentally, exactly the kind of problem that gets cheaper when the page learns in real time instead of in quarters. The product page and the checkout are mostly solved. The expensive, unoptimized middle is where the next 33 percent is sitting.

## LinkedIn series

**Post 1 (Ben Vigoda, Founder & Chief Scientist)**

Here is the thing we learned building this, and it took me a while to accept it.

On a fast-moving fashion brand the lift would hold for a week and then vanish within hours, on its own, because shopper interest, competitor pricing, and new drops had moved faster than our statistics could confirm. The fix was to act before the data was conclusive.

You have to move faster than the speed of statistics. That is the whole idea, and most teams have not caught up to it yet. We stopped optimizing for the shopper who already left and started optimizing for the one still scrolling.

**Post 2 (Noah Maffitt, Chief Growth Officer)**

"We would just build this ourselves."

Fair instinct, and for a team like JTV's, a real option. So here is the honest version.

The hard part is not a recommendation widget. An AI feed that adapts to each shopper as they scroll, learning from the live session instead of waiting for a trend to become statistically significant, working on the first-time visitor and the brand-new SKU. The learning system came out of roughly 35 million dollars of DARPA-funded research, and it is what we maintain so your team does not have to.

Build-versus-buy here is not "can we." It is "is this the thing we want our best engineers spending two years on." For most teams, the answer is no.

**Post 3 (Ben Vigoda, Founder & Chief Scientist)**

A video-commerce model built for cable is migrating to digital and marketplaces, where the on-site discovery experience has to do the selling.

A grid of pretty photos does not solve that. Neither does a search box, because it asks the shopper to already know what they want.

An AI feed that adapts to each shopper as they scroll, learning from the live session instead of waiting for a trend to become statistically significant, surfacing the next best thing and the one detail that resolves the doubt they have not voiced. It learns them in the session, not over a quarter.

For JTV, discovery is the moat. Most teams just have not pointed their best technology at it yet.

## Email drip

**Day 0 | Subject: the page between your ad and your checkout**

Hi Kevin,

JTV is moving a video-commerce model off cable and onto digital, and a scrolling, learning feed is the closest digital analog to what made the channel work.

We built an AI that turns the few seconds after a shopper lands into a feed that adapts as they scroll, surfacing the next best product instead of making them dig. In controlled A/B tests, the headline result was this: a 36 percent average lift in revenue per session across 25 brands and millions of sessions. In jewelry specifically, the lift averaged 33 percent.

It learns from the live session, so our team adds a JavaScript tag in about thirty minutes, no replatform, and you run it as a controlled A/B test on a slice of traffic.

Worth fifteen minutes to show you what it would look like on a JTV page?

Noah Maffitt
Chief Growth Officer, Product Genius

**Day 3 | Subject: the proof behind the number, without cherry-picking**

Hi Kevin,

Quick follow-up with the proof, since the number deserves a footnote.

We ran randomized A/B tests: half of traffic saw the normal site, half saw the same site with our feed added. We measured revenue per session, and we averaged the lift across every day of the test, not just the strong days at the end, so the number is conservative. Jewelry brands averaged 33 percent.

The mechanism behind it is a model that adapts to each shopper in the moment rather than waiting for a trend to become significant. On a fast-moving brand, that was the entire difference between a lift that held and one that evaporated by lunch.

I can send the whitepaper with the learning curves, or walk you through it live. Which is easier?

Noah Maffitt
Chief Growth Officer, Product Genius

**Day 7 | Subject: the build-versus-buy question, answered honestly**

Hi Kevin,

A team as capable as yours has surely asked whether you would just build this. Fair question, so here is the straight answer.

The hard part is not the widget. It is a learning system that adapts faster than statistics can confirm a change, works without third-party data, and performs on the first-time visitor and the new SKU. The learning system came out of roughly 35 million dollars of DARPA-funded research, and it is what we maintain so your team can stay on the roadmap they care about.

On your side it is a tag and an API call, run as a controlled A/B test, not a platform project. If the instinct is still to build, I am glad to be a sounding board on what that actually takes. No pitch.

Noah Maffitt
Chief Growth Officer, Product Genius

**Day 12 | Subject: a test, not a leap of faith**

Hi Kevin,

Last note from me, and it is the lowest-risk way to settle this.

We do not ask you to believe the number. We ask you to run the same randomized A/B test we ran, on a slice of your traffic, with revenue per session as the metric. Our team adds a JavaScript tag in about thirty minutes, no replatform, and you run it as a controlled A/B test on a slice of traffic. If the lift is not there, you have lost almost nothing.

If now is not the moment, no problem, and I will stop landing in your inbox. If you want to see it on a real JTV page first, reply with a time and I will bring the mockup.

Either way, I think the discovery problem is the most interesting one in your category, and it is the natural place to extend what you have already built.

Noah Maffitt
Chief Growth Officer, Product Genius

_QA: clean. No em-dashes, no banned phrases, no unsupported numbers._