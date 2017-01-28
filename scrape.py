import re
import collections

urlbase = 'http://www.cherryblossom.org/'
women_urls = [
    'results/2012/2012cucb10m-f.htm',
    'results/2011/2011cucb10m-f.htm',
    'results/2010/2010cucb10m-f.htm',
    'results/2009/09cucb-F.htm',   # results are written in html, harder to parse
    'results/2008/women.htm',
    'results/2007/women.htm',
    'results/2006/women.htm',      # columns "Hometown" and "Net time" are munged together
    'results/2005/CB05-F.htm',
    'results/2004/women.htm',
    'results/2003/CB03-F.HTM',
    'results/2002/ooff.htm',
    'results/2001/oof_f.html',     # page is missing a header
    'cb003f.htm',
    'cb99f.htm'
]


def mens_url(url):
    """Given a women's url, create the men's url equivalent."""
    url = re.sub('women', 'men', url)
    url = re.sub('f\.', 'm.', url)
    url = re.sub('F\.', 'M.', url)
    return url


def get_year(url):
    """Extract the year from a given url"""
    m = re.search("([0-9][0-9][0-9][0-9])", url)
    if m is not None:
        return int(m.group(1))
    m = re.search("(9[0-9])", url)
    if m is not None:
        return int("19" + m.group(1))
    m = re.search("(0[0-9])", url)
    if m is not None:
        return int("20" + m.group(1))
    return None


# Create a dictionary that maps year to another dictionary of men's and women's urls 
# Example: { 2002: {'m': url_of_2002_mens_results, 'f': url_of_2002_womens_results} }
CHERRY_BLOSSOM_URL_DICT = collections.defaultdict(dict)
for url in women_urls:
    year = get_year(url)
    CHERRY_BLOSSOM_URL_DICT[year]['f'] = url
    CHERRY_BLOSSOM_URL_DICT[year]['m'] = mens_url(url)


def scrape_cherry_blossoms(years, genders, results_file, errors_file):
    """
    Given a list of years and a list of genders and the names of two files, scrape the Cherry Blossoms
    website and write the results in CSV format into the results_file.  Any lines that cannot be processed
    should be written into errors_file.

     The list of genders should be either ['m','f'] or ['m'] or ['f'].

    The header of the results_file should be:
    year,gender,place,name,hometown,age,time

    The time column should be in total minutes.

    Each line in the errors_file should have the following format:
    [URL]:[line that could not be processed]
    For example, when scrape_cherry_blossoms([2010], ['m'], 'results.csv', 'errors.txt') is called, one line in
    errors.txt should be this:
    results/2010/2010cucb10m-m.htm:# Under USATF OPEN guideline
    """
    pass


if __name__ == "__main__":
    for year in CHERRY_BLOSSOM_URL_DICT:
        for gender in CHERRY_BLOSSOM_URL_DICT[year]:
            print year, gender, CHERRY_BLOSSOM_URL_DICT[year][gender]

