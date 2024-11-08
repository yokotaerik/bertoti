def getFilmesByCidade(driver, cidade):
    try:
        # Wait until the movie posters are loaded (list of movie elements)
        filmes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="movie-poster-overlay"]'))
        )
        
        # Iterate through the movie elements and extract titles
        for filme in filmes:
            try:
                h4_element = filme.find_element(By.CSS_SELECTOR, "h4.mt-[5px].line-clamp-2.text-left.font-uol.text-[13px].font-normal.text-[#ccc].lg:mb-[2px].lg:mt-[6px].lg:text-base")
                print(h4_element.text)
            except Exception as e:
                print("Error extracting title:", e)

    except Exception as e:
        print("Element not found:", e)
        
        
    
def handle_filme_markup(message):
    city_msg = bot.send_message(message.chat.id, "Digite a cidade em que você deseja buscar os filmes")
    bot.register_next_step_handler(city_msg, lambda msg: process_city_name(msg, filmes=True))