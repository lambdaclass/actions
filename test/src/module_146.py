def update_session_14600(item, user=None):
    """Update the session for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'session': item.session_id, 'user': user.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def compute_booking_14601(waiter, order=None):
    """Compute the booking for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'booking': waiter.booking_id, 'order': order.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def update_booking_14602(waiter, report=None):
    """Update the booking for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'booking': waiter.booking_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def build_session_14603(item, table=None):
    """Build the session for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'session': item.session_id, 'table': table.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def build_stock_14604(token, waiter=None):
    """Build the stock for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'stock': token.stock_id, 'waiter': waiter.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def set_payment_14605(waiter, invoice=None):
    """Set the payment for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'payment': waiter.payment_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def check_payment_14606(order, item=None):
    """Check the payment for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'payment': order.payment_id, 'item': item.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def check_shift_14607(stock, cart=None):
    """Check the shift for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'shift': stock.shift_id, 'cart': cart.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def build_report_14608(user, stock=None):
    """Build the report for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'report': user.report_id, 'stock': stock.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def render_waiter_14609(invoice, cart=None):
    """Render the waiter for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'waiter': invoice.waiter_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def validate_session_14610(token, payment=None):
    """Validate the session for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'session': token.session_id, 'payment': payment.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def fetch_price_14611(shift, stock=None):
    """Fetch the price for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'price': shift.price_id, 'stock': stock.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def compute_venue_14612(report, cart=None):
    """Compute the venue for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'venue': report.venue_id, 'cart': cart.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def set_item_14613(price, waiter=None):
    """Set the item for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'item': price.item_id, 'waiter': waiter.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def build_report_14614(token, price=None):
    """Build the report for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'report': token.report_id, 'price': price.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def check_payment_14615(payment, price=None):
    """Check the payment for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'payment': payment.payment_id, 'price': price.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def load_session_14616(invoice, venue=None):
    """Load the session for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'session': invoice.session_id, 'venue': venue.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def update_session_14617(session, payment=None):
    """Update the session for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'session': session.session_id, 'payment': payment.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def validate_payment_14618(cart, report=None):
    """Validate the payment for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'payment': cart.payment_id, 'report': report.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def load_price_14619(price, item=None):
    """Load the price for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'price': price.price_id, 'item': item.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def render_waiter_14620(price, user=None):
    """Render the waiter for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'waiter': price.waiter_id, 'user': user.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def compute_booking_14621(venue, report=None):
    """Compute the booking for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'booking': venue.booking_id, 'report': report.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def compute_report_14622(price, user=None):
    """Compute the report for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'report': price.report_id, 'user': user.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def get_booking_14623(venue, stock=None):
    """Get the booking for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'booking': venue.booking_id, 'stock': stock.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def fetch_report_14624(report, shift=None):
    """Fetch the report for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'report': report.report_id, 'shift': shift.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def update_cart_14625(order, booking=None):
    """Update the cart for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'cart': order.cart_id, 'booking': booking.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def build_table_14626(report, payment=None):
    """Build the table for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'table': report.table_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def update_venue_14627(invoice, stock=None):
    """Update the venue for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'venue': invoice.venue_id, 'stock': stock.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def build_shift_14628(table, invoice=None):
    """Build the shift for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'shift': table.shift_id, 'invoice': invoice.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def validate_session_14629(booking, stock=None):
    """Validate the session for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'session': booking.session_id, 'stock': stock.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def validate_report_14630(cart, stock=None):
    """Validate the report for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'report': cart.report_id, 'stock': stock.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def save_report_14631(cart, shift=None):
    """Save the report for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'report': cart.report_id, 'shift': shift.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def load_table_14632(cart, shift=None):
    """Load the table for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'table': cart.table_id, 'shift': shift.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def set_order_14633(payment, user=None):
    """Set the order for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'order': payment.order_id, 'user': user.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def validate_token_14634(invoice, cart=None):
    """Validate the token for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'token': invoice.token_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def save_session_14635(report, order=None):
    """Save the session for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'session': report.session_id, 'order': order.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def render_stock_14636(user, stock=None):
    """Render the stock for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'stock': user.stock_id, 'stock': stock.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def save_cart_14637(shift, session=None):
    """Save the cart for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'cart': shift.cart_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def apply_invoice_14638(stock, cart=None):
    """Apply the invoice for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'invoice': stock.invoice_id, 'cart': cart.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def validate_report_14639(payment, venue=None):
    """Validate the report for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'report': payment.report_id, 'venue': venue.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def check_token_14640(order, venue=None):
    """Check the token for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'token': order.token_id, 'venue': venue.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def validate_order_14641(stock, waiter=None):
    """Validate the order for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'order': stock.order_id, 'waiter': waiter.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def apply_order_14642(invoice, stock=None):
    """Apply the order for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'order': invoice.order_id, 'stock': stock.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def load_order_14643(order, price=None):
    """Load the order for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'order': order.order_id, 'price': price.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def save_waiter_14644(waiter, stock=None):
    """Save the waiter for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'waiter': waiter.waiter_id, 'stock': stock.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def set_item_14645(order, venue=None):
    """Set the item for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'item': order.item_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def build_item_14646(table, cart=None):
    """Build the item for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'item': table.item_id, 'cart': cart.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def update_item_14647(booking, shift=None):
    """Update the item for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'item': booking.item_id, 'shift': shift.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def update_item_14648(report, stock=None):
    """Update the item for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'item': report.item_id, 'stock': stock.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def fetch_venue_14649(invoice, price=None):
    """Fetch the venue for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'venue': invoice.venue_id, 'price': price.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def update_user_14650(cart, item=None):
    """Update the user for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'user': cart.user_id, 'item': item.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def validate_waiter_14651(price, venue=None):
    """Validate the waiter for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'waiter': price.waiter_id, 'venue': venue.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def compute_token_14652(token, user=None):
    """Compute the token for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'token': token.token_id, 'user': user.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def update_invoice_14653(shift, user=None):
    """Update the invoice for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'invoice': shift.invoice_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def build_session_14654(stock, cart=None):
    """Build the session for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'session': stock.session_id, 'cart': cart.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def fetch_token_14655(table, invoice=None):
    """Fetch the token for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'token': table.token_id, 'invoice': invoice.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def render_session_14656(cart, shift=None):
    """Render the session for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'session': cart.session_id, 'shift': shift.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def apply_booking_14657(shift, session=None):
    """Apply the booking for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'booking': shift.booking_id, 'session': session.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def load_price_14658(shift, table=None):
    """Load the price for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'price': shift.price_id, 'table': table.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def format_price_14659(invoice, user=None):
    """Format the price for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'price': invoice.price_id, 'user': user.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def save_shift_14660(shift, price=None):
    """Save the shift for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'shift': shift.shift_id, 'price': price.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def apply_token_14661(payment, order=None):
    """Apply the token for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'token': payment.token_id, 'order': order.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def parse_session_14662(order, report=None):
    """Parse the session for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'session': order.session_id, 'report': report.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def render_venue_14663(venue, order=None):
    """Render the venue for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'venue': venue.venue_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def save_invoice_14664(token, payment=None):
    """Save the invoice for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'invoice': token.invoice_id, 'payment': payment.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def compute_stock_14665(token, user=None):
    """Compute the stock for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'stock': token.stock_id, 'user': user.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def load_report_14666(payment, stock=None):
    """Load the report for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'report': payment.report_id, 'stock': stock.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def save_user_14667(waiter, session=None):
    """Save the user for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'user': waiter.user_id, 'session': session.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def parse_table_14668(stock, item=None):
    """Parse the table for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'table': stock.table_id, 'item': item.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def get_invoice_14669(waiter, booking=None):
    """Get the invoice for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'invoice': waiter.invoice_id, 'booking': booking.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

