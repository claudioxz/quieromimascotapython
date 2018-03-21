
export function getDayName(date, locale) {
    return date.toLocaleDateString(locale, { weekday: 'long' });
}