import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;

public class parsing {
    public static void main(String[] args) throws IOException {
        String url = "https://rozetka.com.ua/ua/notebooks/c80004/filter/";
    parse_category(url);
    }

    private static void parse_category(String url) throws IOException {
        Document doc = Jsoup.connect(url).get();
        Elements nums = doc.select("a.paginator-catalog-l-link");
        int num = Integer.parseInt(nums.last().text());
        for (int i = 0; i < num; i++) {
            String pg = url + String.format("page=%d", i + 1);
            parse_category_page(pg);
        }
    }

    private static void parse_category_page(String url) throws IOException {
        Document doc = Jsoup.connect(url).get();
        Elements tiles = doc.select("div.g-i-tile-i-title");
        for (Element tile : tiles) {
            Element link = tile.select("a").first();
            parse_reviews(link.attr("href") + "comments/");
        }
    }

    private static void parse_reviews(String url) throws IOException {
        Document doc = Jsoup.connect(url).get();
        Elements nums = doc.select("a.paginator-catalog-l-link");
        int num;
        if (nums.size() > 0) {
            num = Integer.parseInt(nums.last().text());
        } else {
            num = 0;
        }
        ArrayList sentiments = new ArrayList();
        for (int i = 0; i < num; i++) {
            String pg = url + String.format("page=%d", i + 1);
            sentiments.add(parse_reviews_page(pg));
        }
    }

    private static ArrayList parse_reviews_page(String url) throws IOException {
        Document doc = Jsoup.connect(url).get();
        ArrayList sentiments = new ArrayList();
        ArrayList optional_array = new ArrayList();
        Elements reviews = doc.select("articles.pp-review-i");
        for (Element review : reviews) {
            Element star = review.select("span.g-rating-stars-i").first();
            Element text = review.select("div.pp-review-text-i").first();
            if (star != null) {
                Elements texts = text.select("div.pp-review-text-i");
                optional_array.add(star.text());
            }
        }
        return sentiments;
    }
}
