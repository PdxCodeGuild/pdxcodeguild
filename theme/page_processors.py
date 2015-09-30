
from mezzanine.pages.page_processors import processor_for

from .models import HomePage
from theme.portfolio.models import PortfolioItem


@processor_for(HomePage)
def home_processor(request, page):
    homepage = HomePage.objects.prefetch_related(
        'slides', 'boxes').select_related(
        'featured_portfolio', 'featured_gallery').get(id=page.homepage.id)
    items = PortfolioItem.objects.published(for_user=request.user).prefetch_related('categories')
    items = items.filter(parent=homepage.featured_portfolio)[:homepage.max_portfolio_items]
    return {"homepage": homepage, 'items': items}
