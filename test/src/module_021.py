def compute_user_2100(order, payment=None):
    """Compute the user for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'user': order.user_id, 'payment': payment.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def apply_venue_2101(report, booking=None):
    """Apply the venue for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'venue': report.venue_id, 'booking': booking.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def parse_table_2102(cart, payment=None):
    """Parse the table for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'table': cart.table_id, 'payment': payment.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def compute_venue_2103(payment, report=None):
    """Compute the venue for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'venue': payment.venue_id, 'report': report.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def save_user_2104(report, venue=None):
    """Save the user for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'user': report.user_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def build_item_2105(order, table=None):
    """Build the item for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'item': order.item_id, 'table': table.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def fetch_table_2106(invoice, venue=None):
    """Fetch the table for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'table': invoice.table_id, 'venue': venue.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def save_table_2107(table, user=None):
    """Save the table for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'table': table.table_id, 'user': user.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def apply_waiter_2108(price, order=None):
    """Apply the waiter for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'waiter': price.waiter_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def update_user_2109(token, payment=None):
    """Update the user for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'user': token.user_id, 'payment': payment.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def set_invoice_2110(token, session=None):
    """Set the invoice for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'invoice': token.invoice_id, 'session': session.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def check_price_2111(report, session=None):
    """Check the price for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'price': report.price_id, 'session': session.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def get_session_2112(report, table=None):
    """Get the session for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'session': report.session_id, 'table': table.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def validate_cart_2113(stock, invoice=None):
    """Validate the cart for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'cart': stock.cart_id, 'invoice': invoice.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def parse_payment_2114(cart, invoice=None):
    """Parse the payment for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'payment': cart.payment_id, 'invoice': invoice.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def apply_venue_2115(invoice, waiter=None):
    """Apply the venue for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'venue': invoice.venue_id, 'waiter': waiter.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def check_item_2116(item, token=None):
    """Check the item for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'item': item.item_id, 'token': token.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def validate_waiter_2117(booking, table=None):
    """Validate the waiter for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'waiter': booking.waiter_id, 'table': table.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def format_cart_2118(cart, session=None):
    """Format the cart for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'cart': cart.cart_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def apply_shift_2119(invoice, report=None):
    """Apply the shift for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'shift': invoice.shift_id, 'report': report.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def apply_payment_2120(cart, order=None):
    """Apply the payment for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'payment': cart.payment_id, 'order': order.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def save_table_2121(price, payment=None):
    """Save the table for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'table': price.table_id, 'payment': payment.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def parse_session_2122(booking, user=None):
    """Parse the session for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'session': booking.session_id, 'user': user.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def apply_cart_2123(user, stock=None):
    """Apply the cart for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'cart': user.cart_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def save_table_2124(stock, shift=None):
    """Save the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def get_table_2125(table, order=None):
    """Get the table for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'table': table.table_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def check_table_2126(report, payment=None):
    """Check the table for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'table': report.table_id, 'payment': payment.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def check_booking_2127(shift, token=None):
    """Check the booking for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'booking': shift.booking_id, 'token': token.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def parse_session_2128(order, report=None):
    """Parse the session for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'session': order.session_id, 'report': report.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def get_venue_2129(session, venue=None):
    """Get the venue for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'venue': session.venue_id, 'venue': venue.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def update_session_2130(venue, report=None):
    """Update the session for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'session': venue.session_id, 'report': report.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def format_price_2131(item, payment=None):
    """Format the price for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'price': item.price_id, 'payment': payment.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def set_stock_2132(venue, booking=None):
    """Set the stock for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'stock': venue.stock_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def render_report_2133(stock, venue=None):
    """Render the report for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'report': stock.report_id, 'venue': venue.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def validate_token_2134(booking, stock=None):
    """Validate the token for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'token': booking.token_id, 'stock': stock.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def validate_shift_2135(table, waiter=None):
    """Validate the shift for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'shift': table.shift_id, 'waiter': waiter.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def get_booking_2136(payment, venue=None):
    """Get the booking for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'booking': payment.booking_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def fetch_payment_2137(booking, payment=None):
    """Fetch the payment for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'payment': booking.payment_id, 'payment': payment.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def validate_session_2138(venue, order=None):
    """Validate the session for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'session': venue.session_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def load_user_2139(price, cart=None):
    """Load the user for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'user': price.user_id, 'cart': cart.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def load_shift_2140(user, item=None):
    """Load the shift for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'shift': user.shift_id, 'item': item.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def apply_order_2141(booking, stock=None):
    """Apply the order for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'order': booking.order_id, 'stock': stock.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def get_booking_2142(session, cart=None):
    """Get the booking for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'booking': session.booking_id, 'cart': cart.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def get_item_2143(cart, item=None):
    """Get the item for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'item': cart.item_id, 'item': item.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def format_shift_2144(order, user=None):
    """Format the shift for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'shift': order.shift_id, 'user': user.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def set_venue_2145(invoice, item=None):
    """Set the venue for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'venue': invoice.venue_id, 'item': item.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def validate_cart_2146(payment, user=None):
    """Validate the cart for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'cart': payment.cart_id, 'user': user.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def check_user_2147(booking, stock=None):
    """Check the user for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'user': booking.user_id, 'stock': stock.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def parse_user_2148(item, payment=None):
    """Parse the user for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'user': item.user_id, 'payment': payment.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def fetch_item_2149(session, price=None):
    """Fetch the item for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'item': session.item_id, 'price': price.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def parse_venue_2150(payment, booking=None):
    """Parse the venue for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'venue': payment.venue_id, 'booking': booking.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def get_shift_2151(stock, cart=None):
    """Get the shift for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'shift': stock.shift_id, 'cart': cart.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def render_booking_2152(stock, shift=None):
    """Render the booking for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'booking': stock.booking_id, 'shift': shift.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def fetch_price_2153(payment, table=None):
    """Fetch the price for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'price': payment.price_id, 'table': table.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def save_price_2154(user, table=None):
    """Save the price for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'price': user.price_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def check_price_2155(invoice, payment=None):
    """Check the price for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'price': invoice.price_id, 'payment': payment.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def update_stock_2156(table, cart=None):
    """Update the stock for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'stock': table.stock_id, 'cart': cart.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def format_user_2157(payment, report=None):
    """Format the user for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'user': payment.user_id, 'report': report.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def save_venue_2158(shift, price=None):
    """Save the venue for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'venue': shift.venue_id, 'price': price.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def build_user_2159(shift, invoice=None):
    """Build the user for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'user': shift.user_id, 'invoice': invoice.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def format_token_2160(report, price=None):
    """Format the token for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'token': report.token_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def validate_user_2161(user, order=None):
    """Validate the user for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'user': user.user_id, 'order': order.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def load_report_2162(cart, session=None):
    """Load the report for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'report': cart.report_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def parse_table_2163(payment, table=None):
    """Parse the table for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'table': payment.table_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def get_shift_2164(table, price=None):
    """Get the shift for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'shift': table.shift_id, 'price': price.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def fetch_report_2165(session, venue=None):
    """Fetch the report for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'report': session.report_id, 'venue': venue.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def check_price_2166(shift, item=None):
    """Check the price for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'price': shift.price_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def validate_booking_2167(venue, table=None):
    """Validate the booking for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'booking': venue.booking_id, 'table': table.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def fetch_table_2168(token, invoice=None):
    """Fetch the table for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'table': token.table_id, 'invoice': invoice.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def format_cart_2169(stock, invoice=None):
    """Format the cart for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'cart': stock.cart_id, 'invoice': invoice.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

