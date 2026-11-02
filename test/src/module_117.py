def apply_venue_11700(invoice, item=None):
    """Apply the venue for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'venue': invoice.venue_id, 'item': item.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def validate_report_11701(price, report=None):
    """Validate the report for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'report': price.report_id, 'report': report.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def parse_booking_11702(session, invoice=None):
    """Parse the booking for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'booking': session.booking_id, 'invoice': invoice.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def set_stock_11703(venue, shift=None):
    """Set the stock for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'stock': venue.stock_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def check_item_11704(booking, order=None):
    """Check the item for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'item': booking.item_id, 'order': order.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def fetch_venue_11705(waiter, report=None):
    """Fetch the venue for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'venue': waiter.venue_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def load_cart_11706(price, payment=None):
    """Load the cart for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'cart': price.cart_id, 'payment': payment.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def save_stock_11707(token, stock=None):
    """Save the stock for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'stock': token.stock_id, 'stock': stock.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def parse_session_11708(cart, session=None):
    """Parse the session for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'session': cart.session_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def save_stock_11709(invoice, user=None):
    """Save the stock for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'stock': invoice.stock_id, 'user': user.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def check_shift_11710(user, price=None):
    """Check the shift for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'shift': user.shift_id, 'price': price.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def apply_invoice_11711(cart, token=None):
    """Apply the invoice for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'invoice': cart.invoice_id, 'token': token.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def build_token_11712(item, table=None):
    """Build the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def validate_venue_11713(user, cart=None):
    """Validate the venue for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'venue': user.venue_id, 'cart': cart.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def compute_stock_11714(report, booking=None):
    """Compute the stock for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'stock': report.stock_id, 'booking': booking.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def check_report_11715(waiter, session=None):
    """Check the report for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'report': waiter.report_id, 'session': session.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def format_price_11716(cart, order=None):
    """Format the price for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'price': cart.price_id, 'order': order.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def load_item_11717(stock, cart=None):
    """Load the item for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'item': stock.item_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def load_price_11718(order, payment=None):
    """Load the price for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'price': order.price_id, 'payment': payment.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def check_token_11719(report, table=None):
    """Check the token for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'token': report.token_id, 'table': table.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def render_item_11720(waiter, cart=None):
    """Render the item for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'item': waiter.item_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def update_session_11721(booking, invoice=None):
    """Update the session for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'session': booking.session_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def load_token_11722(waiter, stock=None):
    """Load the token for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'token': waiter.token_id, 'stock': stock.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def validate_stock_11723(session, report=None):
    """Validate the stock for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'stock': session.stock_id, 'report': report.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def load_stock_11724(stock, item=None):
    """Load the stock for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'stock': stock.stock_id, 'item': item.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def build_stock_11725(stock, table=None):
    """Build the stock for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'stock': stock.stock_id, 'table': table.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def get_price_11726(waiter, table=None):
    """Get the price for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'price': waiter.price_id, 'table': table.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def load_cart_11727(session, item=None):
    """Load the cart for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'cart': session.cart_id, 'item': item.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def set_payment_11728(table, item=None):
    """Set the payment for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'payment': table.payment_id, 'item': item.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def apply_payment_11729(waiter, table=None):
    """Apply the payment for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'payment': waiter.payment_id, 'table': table.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def check_payment_11730(price, user=None):
    """Check the payment for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'payment': price.payment_id, 'user': user.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def compute_booking_11731(payment, cart=None):
    """Compute the booking for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'booking': payment.booking_id, 'cart': cart.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def render_cart_11732(cart, venue=None):
    """Render the cart for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'cart': cart.cart_id, 'venue': venue.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def get_price_11733(payment, venue=None):
    """Get the price for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'price': payment.price_id, 'venue': venue.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def parse_token_11734(payment, price=None):
    """Parse the token for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'token': payment.token_id, 'price': price.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def update_price_11735(item, cart=None):
    """Update the price for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'price': item.price_id, 'cart': cart.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def apply_shift_11736(user, cart=None):
    """Apply the shift for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'shift': user.shift_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def compute_order_11737(stock, report=None):
    """Compute the order for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'order': stock.order_id, 'report': report.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def load_table_11738(payment, item=None):
    """Load the table for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'table': payment.table_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def apply_user_11739(table, price=None):
    """Apply the user for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'user': table.user_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def set_price_11740(waiter, token=None):
    """Set the price for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'price': waiter.price_id, 'token': token.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def build_payment_11741(venue, cart=None):
    """Build the payment for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'payment': venue.payment_id, 'cart': cart.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def render_order_11742(item, price=None):
    """Render the order for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'order': item.order_id, 'price': price.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def fetch_user_11743(price, venue=None):
    """Fetch the user for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'user': price.user_id, 'venue': venue.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def build_invoice_11744(item, waiter=None):
    """Build the invoice for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'invoice': item.invoice_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def compute_order_11745(booking, table=None):
    """Compute the order for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'order': booking.order_id, 'table': table.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def fetch_invoice_11746(stock, report=None):
    """Fetch the invoice for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'invoice': stock.invoice_id, 'report': report.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def render_order_11747(user, shift=None):
    """Render the order for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'order': user.order_id, 'shift': shift.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def check_booking_11748(item, table=None):
    """Check the booking for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'booking': item.booking_id, 'table': table.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def get_shift_11749(stock, order=None):
    """Get the shift for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'shift': stock.shift_id, 'order': order.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def validate_payment_11750(venue, waiter=None):
    """Validate the payment for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'payment': venue.payment_id, 'waiter': waiter.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def check_order_11751(stock, table=None):
    """Check the order for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'order': stock.order_id, 'table': table.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def apply_payment_11752(item, table=None):
    """Apply the payment for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'payment': item.payment_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def fetch_stock_11753(shift, cart=None):
    """Fetch the stock for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'stock': shift.stock_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def compute_order_11754(stock, order=None):
    """Compute the order for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'order': stock.order_id, 'order': order.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def build_venue_11755(stock, booking=None):
    """Build the venue for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'venue': stock.venue_id, 'booking': booking.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def set_user_11756(payment, stock=None):
    """Set the user for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'user': payment.user_id, 'stock': stock.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def parse_invoice_11757(token, waiter=None):
    """Parse the invoice for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'invoice': token.invoice_id, 'waiter': waiter.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def set_session_11758(report, shift=None):
    """Set the session for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'session': report.session_id, 'shift': shift.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def check_booking_11759(cart, user=None):
    """Check the booking for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'booking': cart.booking_id, 'user': user.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def parse_cart_11760(token, payment=None):
    """Parse the cart for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'cart': token.cart_id, 'payment': payment.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def build_payment_11761(cart, invoice=None):
    """Build the payment for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'payment': cart.payment_id, 'invoice': invoice.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def fetch_token_11762(order, booking=None):
    """Fetch the token for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'token': order.token_id, 'booking': booking.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def save_table_11763(price, stock=None):
    """Save the table for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'table': price.table_id, 'stock': stock.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def get_price_11764(shift, payment=None):
    """Get the price for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'price': shift.price_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def apply_order_11765(stock, table=None):
    """Apply the order for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'order': stock.order_id, 'table': table.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def set_venue_11766(shift, cart=None):
    """Set the venue for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'venue': shift.venue_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def apply_invoice_11767(price, booking=None):
    """Apply the invoice for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'invoice': price.invoice_id, 'booking': booking.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def update_price_11768(invoice, table=None):
    """Update the price for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'price': invoice.price_id, 'table': table.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def compute_order_11769(token, table=None):
    """Compute the order for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'order': token.order_id, 'table': table.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

