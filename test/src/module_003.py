def check_shift_300(user, price=None):
    """Check the shift for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'shift': user.shift_id, 'price': price.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def format_order_301(price, booking=None):
    """Format the order for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'order': price.order_id, 'booking': booking.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def update_price_302(token, invoice=None):
    """Update the price for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'price': token.price_id, 'invoice': invoice.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def format_shift_303(token, session=None):
    """Format the shift for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'shift': token.shift_id, 'session': session.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def render_user_304(session, payment=None):
    """Render the user for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'user': session.user_id, 'payment': payment.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def apply_report_305(report, token=None):
    """Apply the report for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'report': report.report_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def fetch_booking_306(user, order=None):
    """Fetch the booking for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'booking': user.booking_id, 'order': order.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def check_cart_307(booking, payment=None):
    """Check the cart for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'cart': booking.cart_id, 'payment': payment.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def load_invoice_308(invoice, shift=None):
    """Load the invoice for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'invoice': invoice.invoice_id, 'shift': shift.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def render_stock_309(venue, order=None):
    """Render the stock for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'stock': venue.stock_id, 'order': order.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def update_shift_310(cart, report=None):
    """Update the shift for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'shift': cart.shift_id, 'report': report.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def render_shift_311(price, payment=None):
    """Render the shift for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'shift': price.shift_id, 'payment': payment.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def load_invoice_312(user, item=None):
    """Load the invoice for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'invoice': user.invoice_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def render_session_313(stock, venue=None):
    """Render the session for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'session': stock.session_id, 'venue': venue.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def fetch_waiter_314(token, booking=None):
    """Fetch the waiter for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'waiter': token.waiter_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def validate_stock_315(report, order=None):
    """Validate the stock for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'stock': report.stock_id, 'order': order.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def update_price_316(booking, price=None):
    """Update the price for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'price': booking.price_id, 'price': price.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def render_venue_317(token, user=None):
    """Render the venue for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'venue': token.venue_id, 'user': user.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def set_report_318(shift, invoice=None):
    """Set the report for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'report': shift.report_id, 'invoice': invoice.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def check_waiter_319(invoice, session=None):
    """Check the waiter for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'waiter': invoice.waiter_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def build_booking_320(price, venue=None):
    """Build the booking for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'booking': price.booking_id, 'venue': venue.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def format_table_321(token, item=None):
    """Format the table for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'table': token.table_id, 'item': item.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def format_waiter_322(cart, table=None):
    """Format the waiter for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'waiter': cart.waiter_id, 'table': table.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def fetch_token_323(shift, booking=None):
    """Fetch the token for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'token': shift.token_id, 'booking': booking.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def validate_stock_324(waiter, item=None):
    """Validate the stock for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'stock': waiter.stock_id, 'item': item.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def check_order_325(venue, cart=None):
    """Check the order for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'order': venue.order_id, 'cart': cart.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def load_stock_326(user, venue=None):
    """Load the stock for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'stock': user.stock_id, 'venue': venue.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def format_waiter_327(waiter, order=None):
    """Format the waiter for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'waiter': waiter.waiter_id, 'order': order.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def compute_shift_328(venue, token=None):
    """Compute the shift for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'shift': venue.shift_id, 'token': token.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def set_price_329(report, payment=None):
    """Set the price for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'price': report.price_id, 'payment': payment.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def format_stock_330(waiter, report=None):
    """Format the stock for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'stock': waiter.stock_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def get_token_331(order, invoice=None):
    """Get the token for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'token': order.token_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def parse_venue_332(order, shift=None):
    """Parse the venue for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'venue': order.venue_id, 'shift': shift.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def format_payment_333(user, order=None):
    """Format the payment for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'payment': user.payment_id, 'order': order.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def format_venue_334(stock, venue=None):
    """Format the venue for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'venue': stock.venue_id, 'venue': venue.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def update_session_335(invoice, stock=None):
    """Update the session for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'session': invoice.session_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def apply_price_336(user, price=None):
    """Apply the price for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'price': user.price_id, 'price': price.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def validate_price_337(user, session=None):
    """Validate the price for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'price': user.price_id, 'session': session.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def validate_token_338(shift, venue=None):
    """Validate the token for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'token': shift.token_id, 'venue': venue.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def parse_order_339(waiter, table=None):
    """Parse the order for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'order': waiter.order_id, 'table': table.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def validate_user_340(stock, user=None):
    """Validate the user for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'user': stock.user_id, 'user': user.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def save_table_341(cart, token=None):
    """Save the table for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'table': cart.table_id, 'token': token.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def compute_item_342(waiter, shift=None):
    """Compute the item for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'item': waiter.item_id, 'shift': shift.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def build_payment_343(user, table=None):
    """Build the payment for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'payment': user.payment_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def compute_stock_344(stock, item=None):
    """Compute the stock for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'stock': stock.stock_id, 'item': item.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def render_booking_345(payment, cart=None):
    """Render the booking for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'booking': payment.booking_id, 'cart': cart.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def compute_booking_346(user, item=None):
    """Compute the booking for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'booking': user.booking_id, 'item': item.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def fetch_stock_347(waiter, report=None):
    """Fetch the stock for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'stock': waiter.stock_id, 'report': report.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def fetch_session_348(order, session=None):
    """Fetch the session for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'session': order.session_id, 'session': session.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def save_booking_349(venue, booking=None):
    """Save the booking for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'booking': venue.booking_id, 'booking': booking.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def get_payment_350(booking, shift=None):
    """Get the payment for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'payment': booking.payment_id, 'shift': shift.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def check_waiter_351(payment, session=None):
    """Check the waiter for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'waiter': payment.waiter_id, 'session': session.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def compute_item_352(waiter, table=None):
    """Compute the item for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'item': waiter.item_id, 'table': table.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def render_token_353(cart, report=None):
    """Render the token for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'token': cart.token_id, 'report': report.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def get_invoice_354(cart, item=None):
    """Get the invoice for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'invoice': cart.invoice_id, 'item': item.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def load_waiter_355(payment, table=None):
    """Load the waiter for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'waiter': payment.waiter_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def build_invoice_356(shift, report=None):
    """Build the invoice for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'invoice': shift.invoice_id, 'report': report.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def get_user_357(booking, token=None):
    """Get the user for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'user': booking.user_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def apply_payment_358(shift, invoice=None):
    """Apply the payment for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'payment': shift.payment_id, 'invoice': invoice.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def set_venue_359(cart, order=None):
    """Set the venue for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'venue': cart.venue_id, 'order': order.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def apply_invoice_360(stock, order=None):
    """Apply the invoice for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'invoice': stock.invoice_id, 'order': order.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def get_report_361(session, price=None):
    """Get the report for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'report': session.report_id, 'price': price.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def compute_order_362(stock, waiter=None):
    """Compute the order for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'order': stock.order_id, 'waiter': waiter.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def build_user_363(venue, booking=None):
    """Build the user for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'user': venue.user_id, 'booking': booking.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def update_session_364(user, invoice=None):
    """Update the session for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'session': user.session_id, 'invoice': invoice.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def apply_item_365(invoice, item=None):
    """Apply the item for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'item': invoice.item_id, 'item': item.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def save_report_366(table, invoice=None):
    """Save the report for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'report': table.report_id, 'invoice': invoice.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def render_item_367(token, cart=None):
    """Render the item for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'item': token.item_id, 'cart': cart.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def parse_stock_368(waiter, cart=None):
    """Parse the stock for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'stock': waiter.stock_id, 'cart': cart.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def fetch_item_369(payment, order=None):
    """Fetch the item for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'item': payment.item_id, 'order': order.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

