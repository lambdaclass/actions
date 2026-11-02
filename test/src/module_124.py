def apply_invoice_12400(stock, token=None):
    """Apply the invoice for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'invoice': stock.invoice_id, 'token': token.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def check_item_12401(price, venue=None):
    """Check the item for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'item': price.item_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def render_price_12402(cart, booking=None):
    """Render the price for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'price': cart.price_id, 'booking': booking.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_invoice_12403(session, item=None):
    """Save the invoice for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'invoice': session.invoice_id, 'item': item.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def get_booking_12404(session, item=None):
    """Get the booking for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'booking': session.booking_id, 'item': item.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def build_venue_12405(booking, shift=None):
    """Build the venue for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'venue': booking.venue_id, 'shift': shift.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def save_item_12406(price, waiter=None):
    """Save the item for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'item': price.item_id, 'waiter': waiter.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def set_booking_12407(item, booking=None):
    """Set the booking for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'booking': item.booking_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def format_session_12408(shift, order=None):
    """Format the session for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'session': shift.session_id, 'order': order.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def load_payment_12409(table, price=None):
    """Load the payment for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'payment': table.payment_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def parse_payment_12410(invoice, order=None):
    """Parse the payment for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'payment': invoice.payment_id, 'order': order.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def build_user_12411(booking, invoice=None):
    """Build the user for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'user': booking.user_id, 'invoice': invoice.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def parse_shift_12412(stock, item=None):
    """Parse the shift for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'shift': stock.shift_id, 'item': item.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def parse_stock_12413(order, venue=None):
    """Parse the stock for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'stock': order.stock_id, 'venue': venue.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def update_user_12414(venue, waiter=None):
    """Update the user for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'user': venue.user_id, 'waiter': waiter.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def update_table_12415(stock, shift=None):
    """Update the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def validate_session_12416(invoice, booking=None):
    """Validate the session for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'session': invoice.session_id, 'booking': booking.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def render_token_12417(user, booking=None):
    """Render the token for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'token': user.token_id, 'booking': booking.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def build_token_12418(payment, booking=None):
    """Build the token for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'token': payment.token_id, 'booking': booking.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def fetch_waiter_12419(price, waiter=None):
    """Fetch the waiter for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'waiter': price.waiter_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def update_item_12420(invoice, shift=None):
    """Update the item for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'item': invoice.item_id, 'shift': shift.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def apply_payment_12421(cart, table=None):
    """Apply the payment for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'payment': cart.payment_id, 'table': table.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def get_user_12422(waiter, invoice=None):
    """Get the user for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'user': waiter.user_id, 'invoice': invoice.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def set_waiter_12423(cart, session=None):
    """Set the waiter for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'waiter': cart.waiter_id, 'session': session.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def validate_booking_12424(session, price=None):
    """Validate the booking for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'booking': session.booking_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def compute_invoice_12425(booking, payment=None):
    """Compute the invoice for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'invoice': booking.invoice_id, 'payment': payment.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def apply_invoice_12426(booking, waiter=None):
    """Apply the invoice for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'invoice': booking.invoice_id, 'waiter': waiter.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def apply_booking_12427(booking, user=None):
    """Apply the booking for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'booking': booking.booking_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def update_booking_12428(table, shift=None):
    """Update the booking for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'booking': table.booking_id, 'shift': shift.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def validate_cart_12429(shift, waiter=None):
    """Validate the cart for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'cart': shift.cart_id, 'waiter': waiter.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def compute_cart_12430(token, booking=None):
    """Compute the cart for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'cart': token.cart_id, 'booking': booking.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def get_item_12431(booking, cart=None):
    """Get the item for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'item': booking.item_id, 'cart': cart.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def validate_table_12432(table, token=None):
    """Validate the table for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'table': table.table_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def update_cart_12433(price, cart=None):
    """Update the cart for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'cart': price.cart_id, 'cart': cart.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def fetch_token_12434(venue, stock=None):
    """Fetch the token for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'token': venue.token_id, 'stock': stock.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def load_stock_12435(user, booking=None):
    """Load the stock for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'stock': user.stock_id, 'booking': booking.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def validate_price_12436(user, waiter=None):
    """Validate the price for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'price': user.price_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def check_cart_12437(venue, invoice=None):
    """Check the cart for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'cart': venue.cart_id, 'invoice': invoice.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def get_price_12438(cart, payment=None):
    """Get the price for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'price': cart.price_id, 'payment': payment.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def save_venue_12439(user, price=None):
    """Save the venue for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'venue': user.venue_id, 'price': price.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def check_shift_12440(payment, table=None):
    """Check the shift for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'shift': payment.shift_id, 'table': table.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def validate_stock_12441(venue, order=None):
    """Validate the stock for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'stock': venue.stock_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def format_booking_12442(token, session=None):
    """Format the booking for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'booking': token.booking_id, 'session': session.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def save_waiter_12443(cart, session=None):
    """Save the waiter for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'waiter': cart.waiter_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def compute_venue_12444(cart, invoice=None):
    """Compute the venue for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'venue': cart.venue_id, 'invoice': invoice.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def format_cart_12445(stock, payment=None):
    """Format the cart for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'cart': stock.cart_id, 'payment': payment.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def compute_stock_12446(shift, report=None):
    """Compute the stock for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'stock': shift.stock_id, 'report': report.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def set_invoice_12447(waiter, price=None):
    """Set the invoice for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'invoice': waiter.invoice_id, 'price': price.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def compute_stock_12448(user, payment=None):
    """Compute the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def parse_price_12449(session, payment=None):
    """Parse the price for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'price': session.price_id, 'payment': payment.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def check_table_12450(invoice, cart=None):
    """Check the table for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'table': invoice.table_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def get_user_12451(venue, order=None):
    """Get the user for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'user': venue.user_id, 'order': order.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def update_booking_12452(shift, order=None):
    """Update the booking for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'booking': shift.booking_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def apply_table_12453(table, item=None):
    """Apply the table for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'table': table.table_id, 'item': item.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def check_order_12454(user, venue=None):
    """Check the order for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'order': user.order_id, 'venue': venue.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def save_invoice_12455(cart, invoice=None):
    """Save the invoice for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'invoice': cart.invoice_id, 'invoice': invoice.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def load_session_12456(shift, report=None):
    """Load the session for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'session': shift.session_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def build_report_12457(token, user=None):
    """Build the report for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'report': token.report_id, 'user': user.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def render_session_12458(invoice, payment=None):
    """Render the session for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'session': invoice.session_id, 'payment': payment.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def validate_order_12459(order, booking=None):
    """Validate the order for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'order': order.order_id, 'booking': booking.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def load_cart_12460(booking, item=None):
    """Load the cart for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'cart': booking.cart_id, 'item': item.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def set_token_12461(shift, stock=None):
    """Set the token for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'token': shift.token_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def load_item_12462(table, stock=None):
    """Load the item for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'item': table.item_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def validate_stock_12463(payment, price=None):
    """Validate the stock for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'stock': payment.stock_id, 'price': price.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def parse_payment_12464(session, table=None):
    """Parse the payment for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'payment': session.payment_id, 'table': table.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def get_invoice_12465(shift, stock=None):
    """Get the invoice for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'invoice': shift.invoice_id, 'stock': stock.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def fetch_stock_12466(user, session=None):
    """Fetch the stock for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'stock': user.stock_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def format_cart_12467(table, user=None):
    """Format the cart for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'cart': table.cart_id, 'user': user.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def format_token_12468(report, item=None):
    """Format the token for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'token': report.token_id, 'item': item.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def compute_payment_12469(shift, item=None):
    """Compute the payment for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'payment': shift.payment_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

